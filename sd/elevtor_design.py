enum ElevatorStatus {
    MOVING,
    WAITING
}

enum MovingDIrection {
    UP,
    DOWN
}

public class Door {
    Boolean open = False
    public void open_door(){
        this.open = True
    }
    public void close_door(){
        this.open = False
    }
}


public class Elevator {

    private ElevatorStatus status = ElevatorStatus.WAITING
    private MovingDirection direction
    private Door door
    private Int currentFloor;
    private List<Int> floor_requests;

    public void move(){
        if status == ElevatorStatus.WAITING:
            return

        next_floor = this.getNextFloor()
        if next_floor == -1:
            status = ElevatorStatus.WAITING
            return
        
        if next_floor > currentFloor:
            direction = MovingDIrection.UP
        elif next_floor < currentFloor:
            direction = MovingDIrection.DOWN
        else:
            this.unLoadPassengers()
            status = ElevatorStatus.WAITING
            return

        if direction == MovingDIrection.DOWN:
            currentFloor--
        elif direction == MovingDIrection.UP:
            currentFloor++
    }

    public void unLoadPassengers(){
        status = ElevatorStatus.WAITING
        door.open()
        # unload
        wait(inf)
        door.close()
    }

    public Int getCurrentFloor(){
        return currentFloor
    }

    private Int getNextFloor(){
        # get next floor to be services according to the current direction
        # if no floors to be serviced => return -1 
    }

}

public class ElevatorController {

    private List<Int> floors
    private List<Elevator> elevators

    public void ElevatorController(List<Elevator> elevators){
        this.elevators = elevators
    }

    public void register_call(floor_number){
        # registers a call for this floor
        floors[floor_number] = True
    }

    public void schedule_jobs(){
        # schedule all elevator request to an appropriate elevator
        # this can get fairly complex , depends on which scheduling algos we use
    }


}


public class ElevatorSystem {

    public void main(){

        Elevator ele1 = new Elevator()
        Elevator ele2 = new Elevator()
        Elevator ele3 = new Elevator()

        List<Elevator> el_list = [ele1, ele2, ele3]

        ElevatorController controller = new ElevatorController(el_list)

        # seperate threads will keep on polling elevator
        # Thread 1 .. n
        while True:
            for e in el_list:
                e.move()
        
        # registering calls for specefic floors
        controller.register_call(5)
        controller.register_call(2)
        controller.register_call(3)

    }

}