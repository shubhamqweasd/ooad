public class BillingSystem {
    public void main() {
        
        Organisation docprime = new Organisation('docprime')
        docprime.add_billing_account(new BillingAccount())
        docprime.add_bank_account(new IndianBankAccount())

        # add some products to organisation
        docprime.add_product(new OneTimeProduct())
        docprime.add_product(new SubscriptionProduct())

        OrganisationCustomer shubham = new OrganisationCustomer(docprime)
        PaymentMode shubham_credit_card = new CreditCard('XXXX-XXXX-XXXX-XXXX', 123, 'Shubham')
        shubham.add_payment_mode(shubham_credit_card)

        shubham.create_token()
        shbham.make_payment(docprime.private_key, product1)

        
    }
}