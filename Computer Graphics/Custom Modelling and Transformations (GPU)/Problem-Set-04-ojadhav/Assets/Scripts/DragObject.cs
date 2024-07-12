using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DragObject : MonoBehaviour
{
    MeshRenderer mr;
    MeshFilter mf;
    Material mat;

    Camera mainCamera;

    [SerializeField] Transform coord;

    private const string shaderName = "CubeShader";
    [SerializeField] private Color CubeColor = new Color(255f / 255f, 255f / 255f, 0f / 255f);

    Vector3 initialPos, newPos;

    Vector3[] vertices;
    int[] triangles;

    string type;

    private Vector2 dr;
    private float R = 5f;

    float srType = 0;

    Vector3 v0 = new Vector3 (-0.5f, -0.5f, 0.5f),
    v1 = new Vector3 (0.5f, -0.5f, 0.5f),
    v2 = new Vector3 (0.5f, -0.5f, -0.5f),
    v3 = new Vector3 (-0.5f, -0.5f, -0.5f),
    v4 = new Vector3 (-0.5f, 0.5f, 0.5f),
    v5 = new Vector3 (0.5f, 0.5f, 0.5f),
    v6 = new Vector3 (0.5f, 0.5f, -0.5f),
    v7 = new Vector3 (-0.5f, 0.5f, -0.5f);

    public void setType(string s){
        type = s;
    }

    void Awake(){
        vertices = new Vector3[] {
            v0, //0
            v1, //1
            v2, //2
            v3, //3
            v4, //4
            v5, //5
            v6, //6
            v7 //7

        };

        triangles = new int[] {
            //bottom
            2, 1, 0,
            3, 2, 0,

            //top
            4, 5, 6,
            4, 6, 7,

            //front
            2, 3, 7,
            2, 7, 6,

            // back
            0, 1, 4,
            1, 5, 4,

            // right
            1, 2, 6,
            1, 6, 5,

            // left
            7, 3, 0,
            4, 7, 0
        };

        Mesh m = new Mesh();
        m.vertices = vertices;
        m.triangles = triangles;
        m.Optimize();
        m.RecalculateNormals();

        mainCamera = Camera.main;
        mr = GetComponent<MeshRenderer>();
        mf = GetComponent<MeshFilter>();
        mf.mesh = m;
        mat = new Material(Shader.Find(shaderName));
        mr.material = mat;
    }

    void Update(){
        mat.SetColor("_CubeColor", CubeColor);
    }

    void OnMouseDown(){
        Vector3 mp = Input.mousePosition;
        initialPos = mainCamera.ScreenToWorldPoint(mp) - transform.position;
    }

    void OnMouseDrag(){
        if(type == "XY"){
            Vector3 mp = mainCamera.ScreenToWorldPoint(Input.mousePosition);
            newPos = mp - initialPos;
            newPos.z = 0;
            mat.SetVector("_newPos", newPos);
        }
        else if(type == "XZ"){
            Vector3 mp = mainCamera.ScreenToWorldPoint(Input.mousePosition);
            newPos = mp - initialPos;
            float temp = newPos.y;
            newPos.y = 0;
            newPos.z = temp; 
            mat.SetVector("_newPos", newPos);
        }
        else if(type == "ROT"){
            Vector2 mp = Input.mousePosition;
            dr = mp - new Vector2(initialPos.x, initialPos.y);
            dr /= dr.magnitude;
            Vector3 n = new Vector3(dr.y/dr.magnitude, -dr.x/dr.magnitude, 0);
            float theta = dr.magnitude/R;
            transform.Rotate(n, theta);
            srType = 1;
            mat.SetFloat("_theta", theta);
        }else if(type == "Scale"){
            Vector2 mp = mainCamera.ScreenToWorldPoint(Input.mousePosition);
            srType = 2;
            transform.localScale += new Vector3(mp.x, mp.y, 1);
            mat.SetVector("_scVector", dr);
        }

        mat.SetFloat("_sr", srType);
    }

}
