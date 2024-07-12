using UnityEngine;

public class MovementController : MonoBehaviour
{
    public float currentSpeed, maxSpeed, acceleration, deceleration, rotSpeed;

    void Start()
    {

    }

    // Update is called once per frame
    void Update()
    {
        MovePlayer();
    }

    void MovePlayer()
    {
        // Get the Forward/Backward input
        float verticalInput = Input.GetAxisRaw("Vertical");

        // Calculate the acceleration input value based on the verticalInput
        float accelerationInput = verticalInput * acceleration * Time.deltaTime;

        // If player input is W or S, add the acceleration to the player's current speed
        if (verticalInput != 0 && Mathf.Abs(currentSpeed) < maxSpeed)
        {
            currentSpeed += accelerationInput;
        }
        else if (currentSpeed != 0)
        {
            // else get the opposite sign of current speed and calculate deceleration value
            float decelerationValue = Mathf.Sign(-currentSpeed) * deceleration * Time.deltaTime;
            // if absolute deceleration value is lesser than the absolute currentspeed value then add the deceleration value to the currentspeed else set current speed to 0 
            currentSpeed = Mathf.Abs(currentSpeed) < Mathf.Abs(decelerationValue) ? 0 : currentSpeed + decelerationValue;
        }

        // Get the Left/Right rotation input
        float horizontalInput = Input.GetAxis("Horizontal");
        horizontalInput *= rotSpeed;
        horizontalInput *= Time.deltaTime;

        // Moving the object
        this.transform.Translate(Vector3.forward * Time.deltaTime * currentSpeed);
        this.transform.Rotate(0, horizontalInput, 0);
    }
}
