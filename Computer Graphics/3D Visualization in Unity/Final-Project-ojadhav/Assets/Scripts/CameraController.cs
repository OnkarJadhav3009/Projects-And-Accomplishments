using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CameraController : MonoBehaviour
{

    Vector4[] possiblePos;

    [SerializeField] private Transform control0, control1, control2, control3, target;

    bool lookAtTarget = true;

    [SerializeField] Camera mainCam;


    [SerializeField] GameObject startingScreen, helpScreen, buttonScreen; 

    float pitch, yaw;

    [Range(8, 512)] [SerializeField] private int curvePoints = 16;
    int i = 0;

    Matrix4x4 splineMatrix = new Matrix4x4(
                        new Vector4(-1f,  3f, -3f, 1f), 
                        new Vector4( 3f, -6f,  3f, 0f), 
                        new Vector4(-3f,  3f,  0f, 0f),
                        new Vector4( 1f,  0f,  0f, 0f) 
                    );

    void Update()
    {   
        possiblePos = calcSpline();
        if (lookAtTarget){
            mainCam.transform.position = new Vector3(possiblePos[(int)i/12].x, possiblePos[(int)i/12].y, possiblePos[(int)i/12].z);
            mainCam.transform.LookAt(target);
            
        }
        else{
            startingScreen.SetActive(false);
            buttonScreen.SetActive(true);
            MoveCam();
        }

        i += 1;
        if((int)i/12 == possiblePos.Length){
            lookAtTarget = false;
            i = 0;
        }
        
    }

    Vector4[] calcSpline(){
        List<Vector4> pos = new List<Vector4>();
        for (int i = 0; i < curvePoints; i++) {
                float u = (float)i / (float)(curvePoints - 1);
                Vector4 uRow = new Vector4(u*u*u, u*u, u, 1f);
                Matrix4x4 controlMatrix = new Matrix4x4(
                   new Vector4(control0.position.x, control0.position.y, control0.position.z, 0f),
                   new Vector4(control1.position.x, control1.position.y, control1.position.z, 0f),
                   new Vector4(control2.position.x, control2.position.y, control2.position.z, 0f),
                   new Vector4(control3.position.x, control3.position.y, control3.position.z, 0f)
                );
                
                Vector4 splinePointPosition = controlMatrix * splineMatrix * uRow;
                pos.Add(splinePointPosition);
        }
        return pos.ToArray();
    }


    void MoveCam(){
        if(Input.GetKey(KeyCode.W)){
            mainCam.transform.localPosition += mainCam.transform.forward * 0.1f;
        }

        if(Input.GetKey(KeyCode.S)){
            mainCam.transform.localPosition += mainCam.transform.forward * -0.1f;
        }

        if(Input.GetKey(KeyCode.Mouse2) || Input.GetKey(KeyCode.Mouse1)){
            yaw += Input.GetAxis("Mouse X") * 2f;
            pitch -= Input.GetAxis("Mouse Y") * 2f;
            mainCam.transform.localEulerAngles = new Vector3(pitch, yaw, 0);
        }

        if(Input.GetKey(KeyCode.Space)){
            mainCam.transform.localPosition += mainCam.transform.up * 0.1f;
        }

        if(Input.GetKey(KeyCode.LeftControl)){
            mainCam.transform.localPosition += mainCam.transform.up * -0.1f;
        }

        if(Input.GetKey(KeyCode.A)){
            mainCam.transform.localPosition += mainCam.transform.right * -0.1f;
        }

        if(Input.GetKey(KeyCode.D)){
            mainCam.transform.localPosition += mainCam.transform.right * 0.1f;
        }

    }

}
