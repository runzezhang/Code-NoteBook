// 题目：设计Booking System

// 目前系统里有两家Hotel

// Hotel目前有两种房间类型：SINGLE和DOUBLE

// Booking System能够支持搜索，输入日期 和 人数， 能够返回住得下
// 的Hotels

// 能够支持预定

// 能够取消预定

// 需要实现BookingSystem class

// Have you met this question in a real interview?  
// Example
// Hotel(1) // 创建hotel id=1
// Hotel(2) // 创建hotel id=2
// Room(1, 1, "Single")  // 创建room，第一个参数是room属于hotel_1, type是单间
// Room(1, 2, "Single")  
// Room(2, 1, "Single")
// Room(2, 2, "Double")  // 创建room，第一个参数是room属于hotel_2, type是标间
// searchHotelRequest("2013-01-06", "2013-10-10", 3)
// searchHotelRequest("2013-01-01", "2013-10-10", 2)
// roomsNeeded("Single", 1, "Double", 1)
// roomsNeeded("Single", 1)
// reservationRequest(2, "2013-01-04", "2013-01-06", 1) // 第一个参数是从hotel_2当中预定
// reservationRequest(1, "2013-01-06", "2013-10-10", 2) // 第一个参数是从hotel_1当中预定
// search result: 2;
// *****************************

// search result: 1;2;
// *****************************

// Hotel Id: 2
// Printing Cache ...
// Search Request -> Start date is: Jan 1, 2013 12:00:00 AM, End date is: Oct 10, 2013 12:00:00 AM
// Value -> For room type: DOUBLE, available rooms are: 2; . For room type: SINGLE, available rooms are: 1; . 

// Search Request -> Start date is: Jan 4, 2013 12:00:00 AM, End date is: Jan 6, 2013 12:00:00 AM
// Value -> For room type: DOUBLE, available rooms are: . For room type: SINGLE, available rooms are: . 

// *****************************

// Hotel Id: 1
// Printing Cache ...
// Search Request -> Start date is: Jan 1, 2013 12:00:00 AM, End date is: Oct 10, 2013 12:00:00 AM
// Value -> For room type: DOUBLE, available rooms are: . For room type: SINGLE, available rooms are: 1; 2; . 

// Search Request -> Start date is: Jan 6, 2013 12:00:00 AM, End date is: Oct 10, 2013 12:00:00 AM
// Value -> For room type: DOUBLE, available rooms are: . For room type: SINGLE, available rooms are: 2; . 

// *****************************

/**
* 本参考程序来自九章算法，由 @马同学 提供。版权所有，转发请注明出处。
* - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
* - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
* - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
* - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code
*/

import java.util.Map.Entry;

public class BookingSystem {
  private List<Hotel> hotels;

  public BookingSystem() {
    hotels = new ArrayList<>();
  }

  public List<Hotel> searchHotel(SearchHotelRequest request) {
    List<Hotel> availableHotels = new ArrayList<>();
    for (Hotel hotel : hotels) {
      SearchRequest searchRequest = new SearchRequest(request.getStartDate(), request.getEndDate());
      Map<RoomType, List<Room>> searchRes = hotel.handleSearchResult(searchRequest);
      int availableCapacity = 0;
      for (Entry<RoomType, List<Room>> entry : searchRes.entrySet()) {
        availableCapacity += entry.getKey().getCapacity() * entry.getValue().size();
      }
      if (availableCapacity >= request.getGroupSize()) {
        availableHotels.add(hotel);
      }
    }
    return availableHotels;
  }

  public Reservation makeReservation(Hotel hotel, ReservationRequest request) {
    return hotel.makeReservation(request);
  }

  public void cancelReservation(Reservation reservation) {
    reservation.getHotel().cancelReservation(reservation);
  }

  public List<Hotel> getHotels() {
    return hotels;
  }
}

class Hotel {
  public static final int DAY = 1 * 24 * 60 * 60 * 1000;

  private int id;
  private List<Room> rooms;
  private LRUCache cache;

  public Hotel(int id) {
    this.id = id;
    cache = new LRUCache(2);
    rooms = new ArrayList<>();
  }

  public int getId() {
    return this.id;
  }

  public Reservation makeReservation(ReservationRequest request) {
    Reservation reservation = new Reservation(request.getStartDate(), request.getEndDate());

    SearchRequest search = new SearchRequest(request.getStartDate(), request.getEndDate());

    Map<RoomType, List<Room>> roomsAvailable = getAvailableRooms(search);

    Map<RoomType, Integer> roomsNeeded = request.getRoomsNeeded();

    for (Entry<RoomType, Integer> entry : roomsNeeded.entrySet()) {
      RoomType roomType = entry.getKey();
      int roomCount = entry.getValue();

      List<Room> rooms = roomsAvailable.get(roomType);

      // Not enough rooms
      if (entry.getValue() > rooms.size()) {
        cache.put(search, roomsAvailable);
        return null;
      }

      for (int i = 0; i < roomCount; i++) {
        Room room = rooms.remove(0);
        reservation.getRooms().add(room);
      }

      roomsAvailable.put(entry.getKey(), rooms);
    }

    cache.put(search, roomsAvailable);

    for (Room room : reservation.getRooms()) {
      room.makeReservation(reservation.getStartDate(), reservation.getEndDate());
    }

    return reservation;
  }

  public Map<RoomType, List<Room>> handleSearchResult(SearchRequest request) {
    if (cache.containsKey(request)) {
      return cache.get(request);
    }

    Map<RoomType, List<Room>> res = getAvailableRooms(request);

    cache.put(request, res);

    return res;
  }

  public void cancelReservation(Reservation reservation) {
    for (Room room : reservation.getRooms()) {
      room.cancelReservation(reservation);
    }
  }

  public List<Room> getRooms() {
    return rooms;
  }

  private Map<RoomType, List<Room>> getAvailableRooms(SearchRequest request) {
    Map<RoomType, List<Room>> res = new HashMap<>();

    res.put(RoomType.SINGLE, new ArrayList<>());
    res.put(RoomType.DOUBLE, new ArrayList<>());

    for (Room room : rooms) {
      if (room.isValidRequest(request)) {
        List<Room> roomList = res.get(room.getRoomType());
        roomList.add(room);
        res.put(room.getRoomType(), roomList);
      }
    }

    return res;
  }

  public String printCache() {
    return "Hotel Id: " + getId() + "\nPrinting Cache ...\n" + cache.toString() + "*****************************\n";
  }
}

class LRUCache extends LinkedHashMap<SearchRequest, Map<RoomType, List<Room>>> {

  private static final long serialVersionUID = 1L;
  private int capacity;

  public LRUCache(int capacity) {
    super(capacity);
    this.capacity = capacity;
  }

  @Override
  protected boolean removeEldestEntry(Entry<SearchRequest, Map<RoomType, List<Room>>> eldest) {
    // TODO Auto-generated method stub
    return size() > this.capacity;
  }

  private String printAvailableRooms(Map<RoomType, List<Room>> rooms) {
    String res = "";
    for (Entry<RoomType, List<Room>> entry : rooms.entrySet()) {
      res += "For room type: " + entry.getKey() + ", available rooms are: ";
      for (Room room : entry.getValue()) {
        res += room.getId() + "; ";
      }
      res += ". ";
    }
    return res;
  }

  @Override
  public String toString() {
    // TODO Auto-generated method stub

    String res = "";

    for (Entry<SearchRequest, Map<RoomType, List<Room>>> entry : super.entrySet()) {
      res += ("Search Request -> " + entry.getKey().toString() + "\n");
      res += ("Value -> " + printAvailableRooms(entry.getValue()) + "\n");
      res += "\n";
    }

    return res;
  }
}

class Reservation {
  private Hotel hotel = null;
  private Date startDate;
  private Date endDate;
  private List<Room> rooms;

  public Reservation(Date startDate, Date endDate) {
    this.startDate = startDate;
    this.endDate = endDate;
    rooms = new ArrayList<>();
  }

  public void setHotel(Hotel hotel) {
    this.hotel = hotel;
  }

  public Hotel getHotel() {
    return hotel;
  }

  public Date getStartDate() {
    return startDate;
  }

  public Date getEndDate() {
    return endDate;
  }

  public List<Room> getRooms() {
    return rooms;
  }

  @Override
  public String toString() {
    // TODO Auto-generated method stub

    String res = "Hotel is: " + hotel.getId() + ", start date is: " + startDate.toLocaleString() + ", End date is: "
        + endDate.toLocaleString() + ", rooms are: ";

    for (Room room : rooms) {
      res += room.getId() + "; ";
    }
    res += ". ";

    return res;
  }
}

class ReservationRequest {
  private Date startDate;
  private Date endDate;
  private Map<RoomType, Integer> roomsNeeded;

  public ReservationRequest(Date startDate, Date endDate, Map<RoomType, Integer> roomsNeeded) {
    // TODO Auto-generated constructor stub
    this.startDate = startDate;
    this.endDate = endDate;
    this.roomsNeeded = roomsNeeded;
  }

  public Date getStartDate() {
    return startDate;
  }

  public Date getEndDate() {
    return endDate;
  }

  public Map<RoomType, Integer> getRoomsNeeded() {
    return roomsNeeded;
  }
}

enum RoomType {
  SINGLE(1), DOUBLE(2);

  private int capacity;

  RoomType(int capacity) {
    this.capacity = capacity;
  }

  public int getCapacity() {
    return capacity;
  }
}

class Room {
  public static final int DAY = 1 * 24 * 60 * 60 * 1000;

  private int id;
  private RoomType roomType;
  private Set<Date> reservations;

  public Room(int id, RoomType roomType) {
    this.id = id;
    this.roomType = roomType;
    reservations = new HashSet<Date>();
  }

  public boolean isValidRequest(SearchRequest request) {
    Date date = new Date(request.getStartDate().getTime());
    for (; date.before(request.getEndDate()); date.setTime(date.getTime() + DAY)) {
      Date tempDate = new Date(date.getTime());
      if (reservations.contains(tempDate)) {
        return false;
      }
    }
    return true;
  }

  public void makeReservation(Date startDate, Date endDate) {
    Date date = new Date(startDate.getTime());
    for (; date.before(endDate); date.setTime(date.getTime() + DAY)) {
      Date tempDate = new Date(date.getTime());
      reservations.add(tempDate);
    }
  }

  public void cancelReservation(Reservation reservation) {
    Date date = new Date(reservation.getStartDate().getTime());
    for (; date.before(reservation.getEndDate()); date.setTime(date.getTime() + DAY)) {
      Date tempDate = new Date(date.getTime());
      reservations.remove(tempDate);
    }
  }

  public RoomType getRoomType() {
    return roomType;
  }

  public int getId() {
    return this.id;
  }
}

class SearchHotelRequest {
  private Date startDate;
  private Date endDate;
  private int groupSize;

  public SearchHotelRequest(Date startDate, Date endDate, int groupSize) {
    this.startDate = startDate;
    this.endDate = endDate;
    this.groupSize = groupSize;
  }

  public Date getStartDate() {
    return startDate;
  }

  public Date getEndDate() {
    return endDate;
  }

  public int getGroupSize() {
    return groupSize;
  }
}

class SearchRequest {
  private Date startDate;
  private Date endDate;

  public SearchRequest(Date startDate, Date endDate) {
    // TODO Auto-generated constructor stub
    this.startDate = startDate;
    this.endDate = endDate;
  }

  public Date getStartDate() {
    return startDate;
  }

  public Date getEndDate() {
    return endDate;
  }

  @Override
  public String toString() {
    // TODO Auto-generated method stub

    String res = "Start date is: " + startDate.toLocaleString() + ", End date is: " + endDate.toLocaleString();

    return res;
  }

  @Override
  public boolean equals(Object obj) {
    // TODO Auto-generated method stub
    if (obj == this)
      return true;
    if (!(obj instanceof SearchRequest))
      return false;

    SearchRequest request = (SearchRequest) obj;

    return request.startDate == this.startDate && request.endDate == this.endDate;
  }

  @Override
  public int hashCode() {
    // TODO Auto-generated method stub
    int result = 17;
    result = 31 * result + startDate.hashCode();
    result = 31 * result + endDate.hashCode();
    return result;
  }
}
