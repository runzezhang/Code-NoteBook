// Can you design a coffee maker, that take a coffee pack, and can simply make a cup of coffee.

// Coffee pack contains the recipe of the coffee, like how many milk / how many sugar to be added in the coffee
// Coffee maker can make coffee based on the recipe provided by the coffee pack
// Only consider 2 type of ingredients: sugar and milk
// the cost of Plain coffee is 2. Add one portion of milk/sugar will increase the cost by 0.5
// Consider use decorator design pattern
// 设计一个自动咖啡机，加入一袋咖啡包，简单地煮一杯咖啡。

// 每个咖啡包包含有咖啡的配方，如加入了多少牛奶，或加入了多少糖
// 咖啡机可根据咖啡包提供的配方制作咖啡
// 只考虑两种成分成分：糖（sugar）和牛奶（milk）
// 普通咖啡的成本是2元。 加入一份牛奶或糖会使成本增加0.5元
// 考虑使用Decorator Design Pattern 
// Example
// Input:

// pack(2, 3)
// makeCoffee()
// Output:

// Cost for this coffee is: 4.5
// Ingredients for this coffee is: Plain Coffee, Milk, Milk, Sugar, Sugar, Sugar

/**
 * 本参考程序来自九章算法，由 @安助教 提供。版权所有，转发请注明出处。 -
 * 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。 -
 * 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班， - Big Data
 * 项目实战班，算法面试高频题班, 动态规划专题班 - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code
 */

public class CoffeeMaker {

  public Coffee makeCoffee(CoffeePack pack) {
    Coffee coffee = new SimpleCoffee();

    for (int i = 0; i < pack.getNeededMilk(); i++) {
      coffee = new WithMilk(coffee);
    }

    for (int i = 0; i < pack.getNeededSugar(); i++) {
      coffee = new WithSugar(coffee);
    }

    return coffee;
  }
}

class CoffeePack {
  private int neededMilk;
  private int neededSugar;

  public CoffeePack(int neededMilk, int neededSugar) {
    this.neededMilk = neededMilk;
    this.neededSugar = neededSugar;
  }

  public int getNeededMilk() {
    return neededMilk;
  }

  public int getNeededSugar() {
    return neededSugar;
  }
}

interface Coffee {
  public double getCost();

  public String getIngredients();
}

class SimpleCoffee implements Coffee {

  @Override
  public double getCost() {
    // TODO Auto-generated method stub
    return 2;
  }

  @Override
  public String getIngredients() {
    // TODO Auto-generated method stub
    return "Plain Coffee";
  }

}

abstract class CoffeeDecorator implements Coffee {
  protected final Coffee decoratedCoffee;

  public CoffeeDecorator(Coffee coffee) {
    this.decoratedCoffee = coffee;
  }

  public double getCost() {
    return decoratedCoffee.getCost();
  }

  public String getIngredients() {
    return decoratedCoffee.getIngredients();
  }
}

class WithMilk extends CoffeeDecorator {

  public WithMilk(Coffee coffee) {
    super(coffee);
  }

  public double getCost() {
    return super.getCost() + 0.5;
  }

  public String getIngredients() {
    return super.getIngredients() + ", Milk";
  }
}

class WithSugar extends CoffeeDecorator {

  public WithSugar(Coffee coffee) {
    super(coffee);
  }

  public double getCost() {
    return super.getCost() + 0.5;
  }

  public String getIngredients() {
    return super.getIngredients() + ", Sugar";
  }
}