using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class RollingBallAlgorithm : MonoBehaviour {

    private Camera myMainCamera;
    private Vector2 myObjectStartPosition, myMouseStartWorldPosition;
    private Vector2 dr;
    private float R = 5f;
    private Vector2 lMousePositionDown;

    private Transform _transform;
    new public Transform transform {
        get {
            return _transform ?? (_transform = GetComponent<Transform>());
        }
    }

    private void Awake() {
        myMainCamera = Camera.main;
    }

    private void OnMouseDown() {
        lMousePositionDown = Input.mousePosition;
    }

    private void OnMouseDrag() {
        Vector2 lMousePosition = Input.mousePosition;
        dr = lMousePosition - lMousePositionDown;
        dr /= dr.magnitude;
        Vector3 n = new Vector3(dr.y/dr.magnitude, -dr.x/dr.magnitude, 0);
        float theta = dr.magnitude/R;
        Vector3 tempPos = transform.position;
        transform.position = new Vector3(-5,5,5);
        transform.Rotate(n, theta);
        transform.position = tempPos;

    }

} 
