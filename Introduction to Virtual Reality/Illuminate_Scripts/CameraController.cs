using UnityEngine;

public class CameraController : MonoBehaviour
{
    public GameObject player, target;
    public float rotateSpeed, cameraFollowSpeed;

    // Start is called before the first frame update
    void Start()
    {
        // Initialize variables with default values;
        rotateSpeed = 90.0f;
        cameraFollowSpeed = 10.0f;
    }

    // Update is called once per frame
    void Update()
    {
        // Camera always looks at the player
        this.transform.LookAt(player.transform); // REF: https://docs.unity3d.com/ScriptReference/Transform.LookAt.html

        // Smooth camera movement to follow the player
        Vector3 cameraPos = Vector3.Lerp(this.transform.position, target.transform.position, cameraFollowSpeed * Time.deltaTime);
        this.transform.position = cameraPos;

        // Left and Right arrow input to adjust camera position to get a better view of the player
        if (Input.GetKey(KeyCode.LeftArrow))
        {
            target.transform.RotateAround(player.transform.position, new Vector3(0, 1, 0), rotateSpeed * Time.deltaTime);
        }
        if (Input.GetKey(KeyCode.RightArrow))
        {
            target.transform.RotateAround(player.transform.position, new Vector3(0, 1, 0), -rotateSpeed * Time.deltaTime);
        }
    }
}
