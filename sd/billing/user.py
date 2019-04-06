public interface User {
    String name
    Int Id

    void login()
    void register()
    void reset_password()
}

public class OrganisationAdmin implements User {
    private Organisation assigned_to

    public void login(){
        # logs in a OrganisationAdmin who can manage its organization
    }

    public void register(){
        # register a OrganisationAdmin who can manage its organization
    }

    public void reset_password(old_pwd, new_pwd){
        # // reset pwd
    }
}