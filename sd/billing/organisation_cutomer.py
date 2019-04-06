public class OrganisationCustomer {

    private Organisation organisation
    private PaymentMode payment_mode
    private TransactionToken token

    public void OrganisationCustomer(Organisation organisation){
        this.organisation = organisation
    }

    public add_payment_mode(PaymentMode payment_mode){
        this.payment_mode = payment_mode
    }

    public TransactionToken create_token(Base64Key public_key){
        # create a token and return
        if public_key == organisation.public_key:
            token = new TransactionToken()
            return token
    }

    public void make_payment(private_key, Product product){
        if private_key == organisation.private_key:
            # calculate payable amount
            Int amount = product.get_payable_amount()
            # make txn
            Int ref_id = payment_mode.make_txn(amount)
            # if txn is a success
            Transaction txn = new Transaction(TransactionType.CREDIT, amount, this, ref_id, product)
            # credit billing account and save txn
            organisation.billing_account.credit(amount, txn)
            # call organization API to register success on their system
            organisation.register_product_purchase()
    }

}