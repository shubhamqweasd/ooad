public interface Product {
    String name
    String description
    Int mrp
    Int deal_price

    Int get_payable_amount(){}
}

public class OneTimeProduct implement Poduct {

    List<Feature> features = []

    public void add_feature(Feature f){
        features.push(f)
    }

    public Int get_payable_amount(){
        return deal_price
    }

}


public class SubscriptionProduct implement Poduct {

    public Int get_payable_amount(){
        return deal_price
    }

}