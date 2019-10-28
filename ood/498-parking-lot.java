// Design a parking lot.

// see CC150 OO Design for details.
// 设计一个停车场

// 一共有n层，每层m列，每列k个位置
// 停车场可以停摩托车，公交车，汽车
// 停车位分别有摩托车位，汽车位，大型停车位
// 每一列，摩托车位编号范围为[0,k/4)(注：包括0，不包括k/4),汽车停车位编号范围为[k/4,k/4*3)(注：不包括k/4*3),大型停车位编号范围为[k/4*3,k)(注：不包括k)
// 一辆摩托车可以停在任何停车位
// 一辆汽车可以停在一个汽车位或者大型停车位
// 一辆公交车可以停在一列里的连续5个大型停车位。
// n levels, each level has m rows of spots and each row has k spots.So each level has m x k spots.
// The parking lot can park motorcycles, cars and buses
// The parking lot has motorcycle spots, compact spots, and large spots
// Each row, motorcycle spots id is in range [0,k/4)(0 is included, k/4 is not included), compact spots id is in range [k/4,k/4*3)(k/4*3 is not included) and large spots id is in range [k/4*3,k)(k is not included).
// A motorcycle can park in any spot
// A car park in single compact spot or large spot
// A bus can park in five large spots that are consecutive and within same row. it can not park in small spots
// Have you met this question in a real interview?  
// Example
// Example 1

// Input:
// level=1
// num_rows=1
// spots_per_row=11
// parkVehicle("Motorcycle_1")
// parkVehicle("Car_1")
// parkVehicle("Car_2")
// parkVehicle("Car_3")
// parkVehicle("Car_4")
// parkVehicle("Car_5")
// parkVehicle("Bus_1")
// unParkVehicle("Car_5")
// parkVehicle("Bus_1")

// Output:
// true
// true
// true
// true
// true
// true
// false
// true

// Explanation: When there is a "Car_5", there is no "Bus_1".
// Example 2

// Input:
// level=1
// num_rows=1
// spots_per_row=14
// parkVehicle("Motorcycle_1")
// parkVehicle("Motorcycle_2")
// parkVehicle("Motorcycle_3")
// parkVehicle("Car_1")
// parkVehicle("Car_2")
// parkVehicle("Car_3")
// parkVehicle("Motorcycle_4")
// parkVehicle("Car_4")
// parkVehicle("Car_5")
// parkVehicle("Car_6")
// parkVehicle("Car_7")
// parkVehicle("Bus_1")
// unParkVehicle("Car_1")
// unParkVehicle("Motorcycle_4")
// unParkVehicle("Car_3")
// unParkVehicle("Car_6")
// parkVehicle("Bus_1")
// unParkVehicle("Car_7")
// parkVehicle("Bus_1")

// Output:
// true
// true
// true
// true
// true
// true
// true
// true
// true
// true
// true
// false
// false
// true

enum VehicleSize {
  Motorcycle, Compact, Large,
}

// abstract Vehicle class
abstract class Vehicle {
  // Write your code here
  protected int spotsNeeded;
  protected VehicleSize size;
  protected String licensePlate; // id for a vehicle

  protected ArrayList<ParkingSpot> parkingSpots = new ArrayList<ParkingSpot>(); // id for parking where may occupy multi

  public int getSpotsNeeded() {
    return spotsNeeded;
  }

  public VehicleSize getSize() {
    return size;
  }

  /* Park vehicle in this spot (among others, potentially) */
  public void parkInSpot(ParkingSpot spot) {
    parkingSpots.add(spot);
  }

  /* Remove car from spot, and notify spot that it's gone */
  public void clearSpots() {
    for (int i = 0; i < parkingSpots.size(); i++) {
      parkingSpots.get(i).removeVehicle();
    }
    parkingSpots.clear();
  }

  // this need to be implement in subclass
  public abstract boolean canFitInSpot(ParkingSpot spot);

  public abstract void print();
}

class Motorcycle extends Vehicle {
  // Write your code here
  public Motorcycle() {
    spotsNeeded = 1;
    size = VehicleSize.Motorcycle;
  }

  public boolean canFitInSpot(ParkingSpot spot) {
    return true;
  }

  public void print() {
    System.out.print("M");
  }
}

class Car extends Vehicle {
  // Write your code here
  public Car() {
    spotsNeeded = 1;
    size = VehicleSize.Compact;
  }

  public boolean canFitInSpot(ParkingSpot spot) {
    return spot.getSize() == VehicleSize.Large || spot.getSize() == VehicleSize.Compact;
  }

  public void print() {
    System.out.print("C");
  }
}

class Bus extends Vehicle {
  // Write your code here
  public Bus() {
    spotsNeeded = 5;
    size = VehicleSize.Large;
  }

  public boolean canFitInSpot(ParkingSpot spot) {
    return spot.getSize() == VehicleSize.Large;
  }

  public void print() {
    System.out.print("B");
  }
}

class ParkingSpot {
  // Write your code here
  private Vehicle vehicle;
  private VehicleSize spotSize;
  private int row;
  private int spotNumber;
  private Level level;

  public ParkingSpot(Level lvl, int r, int n, VehicleSize sz) {
    level = lvl;
    row = r;
    spotNumber = n;
    spotSize = sz;
  }

  public boolean isAvailable() {
    return vehicle == null;
  }

  /*
   * Checks if the spot is big enough for the vehicle (and is available). This
   * compares the SIZE only. It does not check if it has enough spots.
   */
  public boolean canFitVehicle(Vehicle vehicle) {
    return isAvailable() && vehicle.canFitInSpot(this);
  }

  /* Park vehicle in this spot. */
  public boolean park(Vehicle v) {
    if (!canFitVehicle(v)) {
      return false;
    }
    vehicle = v;
    vehicle.parkInSpot(this);
    return true;
  }

  /* Remove vehicle from spot, and notify level that a new spot is available */
  public void removeVehicle() {
    level.spotFreed();
    vehicle = null;
  }

  public int getRow() {
    return row;
  }

  public int getSpotNumber() {
    return spotNumber;
  }

  public VehicleSize getSize() {
    return spotSize;
  }

  public void print() {
    if (vehicle == null) {
      if (spotSize == VehicleSize.Compact) {
        System.out.print("c");
      } else if (spotSize == VehicleSize.Large) {
        System.out.print("l");
      } else if (spotSize == VehicleSize.Motorcycle) {
        System.out.print("m");
      }
    } else {
      vehicle.print();
    }
  }
}

/* Represents a level in a parking garage */
class Level {
  // Write your code here
  private int floor;
  private ParkingSpot[] spots;
  private int availableSpots = 0; // number of free spots
  private int SPOTS_PER_ROW;

  public Level(int flr, int num_rows, int spots_per_row) {
    floor = flr;
    int SPOTS_PER_ROW = spots_per_row;
    int numberSpots = 0;
    spots = new ParkingSpot[num_rows * spots_per_row];

    // init size for each spot in array spots
    for (int row = 0; row < num_rows; ++row) {
      for (int spot = 0; spot < spots_per_row / 4; ++spot) {
        VehicleSize sz = VehicleSize.Motorcycle;
        spots[numberSpots] = new ParkingSpot(this, row, numberSpots, sz);
        numberSpots++;
      }
      for (int spot = spots_per_row / 4; spot < spots_per_row / 4 * 3; ++spot) {
        VehicleSize sz = VehicleSize.Compact;
        spots[numberSpots] = new ParkingSpot(this, row, numberSpots, sz);
        numberSpots++;
      }
      for (int spot = spots_per_row / 4 * 3; spot < spots_per_row; ++spot) {
        VehicleSize sz = VehicleSize.Large;
        spots[numberSpots] = new ParkingSpot(this, row, numberSpots, sz);
        numberSpots++;
      }
    }

    availableSpots = numberSpots;
  }

  /* Try to find a place to park this vehicle. Return false if failed. */
  public boolean parkVehicle(Vehicle vehicle) {
    if (availableSpots() < vehicle.getSpotsNeeded()) {
      return false; // no enough spots
    }
    int spotNumber = findAvailableSpots(vehicle);
    if (spotNumber < 0) {
      return false;
    }
    return parkStartingAtSpot(spotNumber, vehicle);
  }

  /* find a spot to park this vehicle. Return index of spot, or -1 on failure. */
  private int findAvailableSpots(Vehicle vehicle) {
    int spotsNeeded = vehicle.getSpotsNeeded();
    int lastRow = -1;
    int spotsFound = 0;

    for (int i = 0; i < spots.length; i++) {
      ParkingSpot spot = spots[i];
      if (lastRow != spot.getRow()) {
        spotsFound = 0;
        lastRow = spot.getRow();
      }
      if (spot.canFitVehicle(vehicle)) {
        spotsFound++;
      } else {
        spotsFound = 0;
      }
      if (spotsFound == spotsNeeded) {
        return i - (spotsNeeded - 1); // index of spot
      }
    }
    return -1;
  }

  /*
   * Park a vehicle starting at the spot spotNumber, and continuing until
   * vehicle.spotsNeeded.
   */
  private boolean parkStartingAtSpot(int spotNumber, Vehicle vehicle) {
    vehicle.clearSpots();

    boolean success = true;

    for (int i = spotNumber; i < spotNumber + vehicle.spotsNeeded; i++) {
      success &= spots[i].park(vehicle);
    }

    availableSpots -= vehicle.spotsNeeded;
    return success;
  }

  /* When a car was removed from the spot, increment availableSpots */
  public void spotFreed() {
    availableSpots++;
  }

  public int availableSpots() {
    return availableSpots;
  }

  public void print() {
    int lastRow = -1;
    for (int i = 0; i < spots.length; i++) {
      ParkingSpot spot = spots[i];
      if (spot.getRow() != lastRow) {
        System.out.print("  ");
        lastRow = spot.getRow();
      }
      spot.print();
    }
  }
}

public class ParkingLot {
  private Level[] levels;
  private int NUM_LEVELS;

  // @param n number of leves
  // @param num_rows each level has num_rows rows of spots
  // @param spots_per_row each row has spots_per_row spots
  public ParkingLot(int n, int num_rows, int spots_per_row) {
    // Write your code here
    NUM_LEVELS = n;
    levels = new Level[NUM_LEVELS];
    for (int i = 0; i < NUM_LEVELS; i++) {
      levels[i] = new Level(i, num_rows, spots_per_row);
    }
  }

  // Park the vehicle in a spot (or multiple spots)
  // Return false if failed
  public boolean parkVehicle(Vehicle vehicle) {
    // Write your code here
    for (int i = 0; i < levels.length; i++) {
      if (levels[i].parkVehicle(vehicle)) {
        return true;
      }
    }
    return false;
  }

  // unPark the vehicle
  public void unParkVehicle(Vehicle vehicle) {
    // Write your code here
    vehicle.clearSpots();
  }

  public void print() {
    for (int i = 0; i < levels.length; i++) {
      System.out.print("Level" + i + ": ");
      levels[i].print();
      System.out.println("");
    }
    System.out.println("");
  }}

  #本参考程序来自九章算法，由 @九章算法 提供。版权所有，转发请注明出处。#-九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。#-现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，

  Android 项目实战班，#-
  Big Data 项目实战班，算法面试高频题班,动态规划专题班#-更多详情请见官方网站：http:// www.jiuzhang.com/?source=code

  #

  enum type for Vehicle
  class VehicleSize:Motorcycle=1 Compact=2 Large=3 Other=99

  class Vehicle:#
  Write your
  code here

  def __init__(self):
        self.parking_spots = []
        self.spots_needed = 0
        self.size = None
        self.license_plate = None

  def get_spots_needed(self):
        return self.spots_needed

  def get_size(self):
        return self.size

  def park_in_spot(self, spot):
        self.parking_spots.append(spot)

  def clear_spots(self):
        for spot in self.parking_spots:
            spot.remove_vehicle()
        
        self.parking_spots = []

  def can_fit_in_spot(self, spot):

  raise NotImplementedError('This method should have implemented.')


class Motorcycle(Vehicle):
    # Write your code here
    def __init__(self):
        Vehicle.__init__(self)
        self.spots_needed = 1
        self.size = VehicleSize.Motorcycle

    def can_fit_in_spot(self, spot):
        return True


class Car(Vehicle):
    # Write your code here
    def __init__(self):
        Vehicle.__init__(self)
        self.spots_needed = 1
        self.size = VehicleSize.Compact

    def can_fit_in_spot(self, spot):
        return spot.get_size() == VehicleSize.Large or \
                spot.get_size() == VehicleSize.Compact


class Bus(Vehicle):
    # Write your code here
    def __init__(self):
        Vehicle.__init__(self)
        self.spots_needed = 5
        self.size = VehicleSize.Large

    def can_fit_in_spot(self, spot):
        return spot.get_size() == VehicleSize.Large


class ParkingSpot:
    # Write your code here
    def __init__(self, lvl, r, n, sz):
        self.level = lvl
        self.row = r
        self.spot_number = n
        self.spot_size = sz
        self.vehicle = None

    def is_available(self):
        return self.vehicle == None

    def can_fit_vehicle(self, vehicle):
        return self.is_available() and vehicle.can_fit_in_spot(self)

    def park(self, v):
        if not self.can_fit_vehicle(v):
            return False

        self.vehicle = v
        self.vehicle.park_in_spot(self)
        return True

    def remove_vehicle(self):
        self.level.spot_freed()
        self.vehicle = None

    def get_row(self):
        return self.row
    
    def get_spot_number(self):
        return self.spot_number

    def get_size(self):
        return self.spot_size


class Level:
    # Write your code here
    def __init__(self, flr, num_rows, spots_per_row):
        self.floor = flr
        self.spots_per_row = spots_per_row
        self.number_spots = 0
        self.available_spots = 0;
        self.spots = []
        
        for row in xrange(num_rows):
            for spot in xrange(0, spots_per_row / 4):
                sz = VehicleSize.Motorcycle
                self.spots.append(ParkingSpot(self, row, self.number_spots, sz))
                self.number_spots += 1

            for spot in xrange(spots_per_row / 4, spots_per_row / 4 * 3):
                sz = VehicleSize.Compact
                self.spots.append(ParkingSpot(self, row, self.number_spots, sz))
                self.number_spots += 1

            for spot in xrange(spots_per_row / 4 * 3, spots_per_row):
                sz = VehicleSize.Large
                self.spots.append(ParkingSpot(self, row, self.number_spots, sz))
                self.number_spots += 1

        self.available_spots = self.number_spots
        
    def park_vehicle(self, vehicle):
        if self.get_available_spots() < vehicle.get_spots_needed():
            return False

        spot_num = self.find_available_spots(vehicle)

        if spot_num < 0:
            return False
        return self.park_starting_at_spot(spot_num, vehicle)

    def find_available_spots(self, vehicle):
        spots_needed = vehicle.get_spots_needed()
        last_row = -1
        spots_found = 0
        
        for i in xrange(len(self.spots)):
            spot = self.spots[i]
            if last_row != spot.get_row():
                spots_found = 0
                last_row = spot.get_row()
            if spot.can_fit_vehicle(vehicle):
                spots_found += 1
            else:
                spots_found = 0
            
            if spots_found == spots_needed:
                return i - (spots_needed - 1)

        return -1

    def park_starting_at_spot(self, spot_num, vehicle):
        vehicle.clear_spots()
        success = True

        for i in xrange(spot_num, spot_num + vehicle.get_spots_needed()):
            success = success and self.spots[i].park(vehicle)
        
        if success:
        	self.available_spots -= vehicle.get_spots_needed()
            
        return success

    def spot_freed(self):
        self.available_spots += 1

    def get_available_spots(self):
        return self.available_spots


class ParkingLot:
    # @param {int} n number of leves
    # @param {int} num_rows  each level has num_rows rows of spots
    # @param {int} spots_per_row each row has spots_per_row spots
    def __init__(self, n, num_rows, spots_per_row):
        # Write your code here
        self.levels = []
        for i in xrange(n):
            self.levels.append(Level(i, num_rows, spots_per_row))

	# Park the vehicle in a spot (or multiple spots)
    # Return false if failed
    def park_vehicle(self, vehicle):
        # Write your code here
        for level in self.levels:
            if level.park_vehicle(vehicle):
                return True
        return False

    # unPark the vehicle
    def unpark_vehicle(self, vehicle):
        # Write your code here
        vehicle.clear_spots()