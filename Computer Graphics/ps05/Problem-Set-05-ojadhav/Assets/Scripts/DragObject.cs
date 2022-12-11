using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DragObject : MonoBehaviour
{
    private Vector3 initialPos;
    private float zVal;

    Camera cam;

    void Awake(){
        cam = Camera.main;
    }

    void OnMouseDown()
    {
        zVal = cam.WorldToScreenPoint(gameObject.transform.position).z;
        initialPos = gameObject.transform.position - GetMouseAsWorldPoint();
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
        transform.position = new Vector3(0,19,-60);
    }
}
