public enum OrganisationStatus {
    ACTIVE,
    UNDER_QA,
    BLOCKED,
    CLOSED,
}

public class Organisation {

    private string name
    private OrganisationStatus status
    private List<BankAccount> bank_accounts
    private BankAccount preffered_account
    private Base64Key public_key
    private Base64Key private_key
    private BillingAccount billing_account
    private String success_url
    private String failure_url
    private List<Product> products

    public Organisation(string name){
        this.billing_account = billing_account
        this.name = name 
        this.public_key = new Base64Key()
        this.private_key = new Base64Key()
    }

    public add_billing_account(BillingAccount ba){
        billing_account = ba
    }

    public List<BankAccount> list_accounts(){
        return filtered => bank_accounts
    }

    public void add_bank_account(BankAccount account){
        bank_accounts.push(account)
    }

    public void public register_product_purchase(){
        # call success url to resgister product purchase
    }

}