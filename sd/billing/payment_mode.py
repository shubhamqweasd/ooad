public interface PaymentMode {
    Int id 
    Int make_txn()
    Int refund_txn()
}

public class CreditCard {
    private LongInt card_number
    private String holder_name
    private Int CVV

    public Int make_txn(){
        # make txn and return refernce id
    }

    public Int refund_txn(txn_id){
        # make refund under a txn_id
    }
}

public class DebitCard {
    private LongInt card_number
    private String holder_name
    private Int CVV

    public Int make_txn(){
        # make txn and return refernce id
    }

    public Int refund_txn(txn_id){
        # make refund under a txn_id
    }
}