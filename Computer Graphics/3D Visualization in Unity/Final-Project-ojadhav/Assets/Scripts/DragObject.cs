using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DragObject : MonoBehaviour
{
    private Vector3 initialPos;
    private float zVal;

    Camera cam;
    Rigidbody rb;

    void Awake(){
        cam = Camera.main;
        rb = GetComponent<Rigidbody>();
    }

    void OnMouseDown()
    {
        zVal = cam.WorldToScreenPoint(gameObject.transform.position).z;
        initialPos = gameObject.transform.position - GetMouseAsWorldPoint();
        rb.useGravity = true;
    }

    private Vector3 GetMouseAsWorldPoint()
    {
        Vector3 mousePoint = Input.mousePosition;
        mousePoint.z = zVal;
        return cam.ScreenToWorldPoint(mousePoint);
    }

    void OnMouseDrag()
    {
        transform.position = GetMouseAsWorldPoint() + initialPos;
    }

    public void ResetPos(){
        transform.position = new Vector3(40,40,-20);
        transform.eulerAngles = new Vector3(0,0,0);
        rb.useGravity = false;
    }
}
