public interface BankAccount {
    String bank_name
    String holder_name
    LongInt account_number

    void transfer_money(Int amount)
}

public class USBankAccount implements BankAccount {
    LongInt social_security_number

    public void transfer_money(){
        # this will transfer money from organisation billing account to real bank account
    }
}

public class IndianBankAccount implements BankAccount {
    LongInt ifsc_code

    public void transfer_money(){
        # this will transfer money from organisation billing account to real bank account
    }
    
}