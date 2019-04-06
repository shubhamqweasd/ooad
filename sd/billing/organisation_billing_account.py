public class BillingAccount{

    private float balance = 0
    private List<Transaction> transaction


    public void credit(Int amount, Transaction txn){
        balance += amount
        transaction.push(txn)
    }

    public void debit(Int amount, Transaction txn){
        balance -= amount
        transaction.push(txn)
    }

}