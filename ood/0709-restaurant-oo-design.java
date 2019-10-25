// Description
// 中文
// English
// No food delivery.

// No table reservation

// The table has different size

// The restaurant will choose the smallest table which fit the numbers of people(For example, if the party has 3 people, the restaurant would assign a 4-people table instead of a 10-people table)

// Implement Restaurant Class

// Everytime after calling findTable, takeOrder, checkOut, we will userestaurantDescription to test the program.
// 不能预订座位

// 不能订外卖

// 餐馆的桌子有不同大小

// 餐馆会优先选择适合当前Party最小的空桌

// 需要实现Restaurant Class

// 每次调用findTable, takeOrder, checkOut之后都会调用restaurantDescription, 来验证你的程序是否正确。
// Have you met this question in a real interview?  
// Example
// Example 1

// Input:
// meal(10.0)
// meal(13.0)
// meal(17.0)
// table(4)
// table(4)
// table(10)
// party(3)
// party(7)
// party(4)
// party(6)
// party(1)
// order(1)
// order(2, 3)
// findTable(1)
// findTable(3)
// findTable(4)
// takeOrder(1, 1)
// takeOrder(3, 2)
// checkOut(3)
// findTable(4)

// Output:
// Table: 0, table size: 4, isAvailable: false. No current order for this table.
// Table: 1, table size: 4, isAvailable: true. No current order for this table.
// Table: 2, table size: 10, isAvailable: true. No current order for this table.
// *****************************************

// Table: 0, table size: 4, isAvailable: false. No current order for this table.
// Table: 1, table size: 4, isAvailable: false. No current order for this table.
// Table: 2, table size: 10, isAvailable: true. No current order for this table.
// *****************************************

// Table: 0, table size: 4, isAvailable: false. No current order for this table.
// Table: 1, table size: 4, isAvailable: false. No current order for this table.
// Table: 2, table size: 10, isAvailable: false. No current order for this table.
// *****************************************

// Table: 0, table size: 4, isAvailable: false. Order price: 10.0.
// Table: 1, table size: 4, isAvailable: false. No current order for this table.
// Table: 2, table size: 10, isAvailable: false. No current order for this table.
// *****************************************

// Table: 0, table size: 4, isAvailable: false. Order price: 10.0.
// Table: 1, table size: 4, isAvailable: false. No current order for this table.
// Table: 2, table size: 10, isAvailable: false. Order price: 30.0.
// *****************************************

// Table: 0, table size: 4, isAvailable: false. Order price: 10.0.
// Table: 1, table size: 4, isAvailable: false. No current order for this table.
// Table: 2, table size: 10, isAvailable: true. No current order for this table.
// *****************************************

// Table: 0, table size: 4, isAvailable: false. Order price: 10.0.
// Table: 1, table size: 4, isAvailable: false. No current order for this table.
// Table: 2, table size: 10, isAvailable: false. No current order for this table.
// *****************************************

// Explanation:
// meal(x) means we create a meal, whose price is x
// Example 2

// Input:
// meal(12.0)
// table(4)
// table(4)
// table(10)
// party(13)
// findTable(1)

// Output:
// Table: 0, table size: 4, isAvailable: true. No current order for this table.
// Table: 1, table size: 4, isAvailable: true. No current order for this table.
// Table: 2, table size: 10, isAvailable: true. No current order for this table.
// *****************************************

class NoTableException extends Exception{

    public NoTableException(Party p)
	{
		super("No table available for party size: " + p.getSize());
	}
}

class Meal {
	private float price;
	
	public Meal(float price)
	{
		this.price = price;
	}
	
	public float getPrice()
	{
		return this.price;
	}
}

class Order {
	private List<Meal> meals;
	
	public Order()
	{
		meals = new ArrayList<Meal>();
	}
	
	public List<Meal> getMeals()
	{
		return meals;
	}
	
	public void mergeOrder(Order order)
	{
		if(order != null)
		{
			for(Meal meal : order.getMeals())
			{
				meals.add(meal);
			}
		}
	}
	
	public float getBill()
	{
		int bill = 0;
		for(Meal meal : meals)
		{
			bill += meal.getPrice();
		}
		return bill;
	}
}

class Party {
	private int size;
	
	public Party(int size)
	{
		this.size = size;
	}
	
	public int getSize()
	{
		return this.size;
	}
}

class Table implements Comparable<Table>{
	private int capacity;
	private boolean available;
	private Order order;
	
	public Table(int capacity)
	{
		this.capacity = capacity;
		available = true;
		order = null;
	}
	
	public int getCapacity()
	{
		return this.capacity;
	}
	
	public boolean isAvailable()
	{
		return this.available;
	}
	
	public void markAvailable()
	{
		this.available = true;
	}
	
	public void markUnavailable()
	{
		this.available = false;
	}
	
	public Order getCurrentOrder()
	{
		return this.order;
	}
	
	public void setOrder(Order o)
	{
		if(order == null)
		{
			this.order = o;
		}
		else 
		{
			if(o != null)
			{
				this.order.mergeOrder(o);
			} else {
				this.order = o;
			}
		}
	}

	@Override
	public int compareTo(Table compareTable) {
		// TODO Auto-generated method stub
		return this.capacity - compareTable.getCapacity();
	}
}

public class Restaurant {
	private List<Table> tables;
	private List<Meal> menu;
	
	public Restaurant()
	{
		tables = new ArrayList<Table>();
		menu = new ArrayList<Meal>();
	}
	
	public void findTable(Party p) throws NoTableException
	{
		for(Table t: tables)
		{
			if(t.isAvailable())
			{
				if(t.getCapacity() >= p.getSize())
				{
					t.markUnavailable();
					return;
				}
			}
		}
		throw new NoTableException(p);
	}
	
	public void takeOrder(Table t, Order o)
	{
		t.setOrder(o);
	}
	
	public float checkOut(Table t)
	{
		float bill = 0;
		if(t.getCurrentOrder() != null)
		{
			bill = t.getCurrentOrder().getBill();
		}

		t.markAvailable();
		t.setOrder(null);
		
		return bill;
	}
	
	public List<Meal> getMenu()
	{
		return menu;
	}
	
	public void addTable(Table t)
	{
		tables.add(t);
		Collections.sort(tables);
	}
	
	public String restaurantDescription()
	{
        // Keep them, don't modify.
		String description = "";
		for(int i = 0; i < tables.size(); i++)
		{
			Table table = tables.get(i);
			description += ("Table: " + i + ", table size: " + table.getCapacity() + ", isAvailable: " + table.isAvailable() + ".");
			if(table.getCurrentOrder() == null)
				description += " No current order for this table"; 
			else
				description +=  " Order price: " + table.getCurrentOrder().getBill();
			
			description += ".\n";
		}
		description += "*****************************************\n";
		return description;
	}
}