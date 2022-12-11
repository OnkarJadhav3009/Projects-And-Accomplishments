using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DrawAxes : MonoBehaviour
{
    public void OnDrawGizmos(){

        Gizmos.color = Color.green;
        Gizmos.DrawLine(transform.position, transform.position + Vector3.up * 10);
        for(int i = 0; i < 10; i++){
            Gizmos.DrawLine(transform.position + Vector3.up *i, transform.position + Vector3.right + Vector3.up * i);
            Gizmos.DrawLine(transform.position + Vector3.up *i, transform.position - Vector3.forward + Vector3.up * i);
        }

        Gizmos.color = Color.red;
        Gizmos.DrawLine(transform.position, transform.position + Vector3.right * 10);
        for(int i = 0; i < 10; i++){
            Gizmos.DrawLine(transform.position + Vector3.right *i, transform.position + Vector3.up + Vector3.right * i);
            Gizmos.DrawLine(transform.position + Vector3.right *i, transform.position - Vector3.forward + Vector3.right * i);
        }

        Gizmos.color = Color.blue;
        Gizmos.DrawLine(transform.position, transform.position -Vector3.forward * 10);
        for(int i = 0; i < 10; i++){
            Gizmos.DrawLine(transform.position - Vector3.forward *i, transform.position + Vector3.right - Vector3.forward * i);
            Gizmos.DrawLine(transform.position - Vector3.forward *i, transform.position + Vector3.up - Vector3.forward * i);
        }

    }
}
