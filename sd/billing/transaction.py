public enum TransactionType {
    CREDIT 
    DEBIT
}

public class Transaction {

    private TransactionType type 
    private Int amount
    private OrganisationCustomer customer 
    private DateTime txn_date
    private Int reference_id
    private Product product

    public void Transaction(TransactionType type, Int amount, OrganisationCustomer customer, Int reference_id, Product product){
        this.type = type
        this.amount = amount
        this.customer = customer
        this.reference_id = reference_id
        this.product = product
        this.txn_date = now()
    }

}