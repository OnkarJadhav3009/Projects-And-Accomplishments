using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CPUComputeBowl : MonoBehaviour
{

    Mesh mesh;
    MeshCollider mc;

    Material mat;

    [SerializeField] Transform lightPos, cameraPos;

    public Color ambientColor, specularColor, diffuseColor;

    bool isOn;

    void Start()
    {

        isOn = true;
        mesh = new Mesh();

        mesh.vertices = CalculateVertices();
        mesh.triangles = CalculateTriangles();
        mesh.Optimize();
        mesh.RecalculateNormals();

        gameObject.GetComponent<MeshFilter>().mesh = mesh;
        MeshRenderer mr = gameObject.GetComponent<MeshRenderer>();
        
        mat = new Material(Shader.Find("BowlShader"));
        mr.material = mat;

        MeshCollider mc = gameObject.GetComponent<MeshCollider>();
        mc.sharedMesh = mesh;

    }

    void Update(){

        if(isOn){
            mat.SetFloat("isOn", 1f);
        }
        else{
            mat.SetFloat("isOn", 2f);
        }
        mat.SetVector("lightPos", lightPos.position);
        mat.SetVector("cameraPos", cameraPos.position);
        mat.SetVector("ambientColor", ambientColor);
        mat.SetVector("diffuseColor", diffuseColor);
        mat.SetVector("specularColor", specularColor);
    }

    public void switchONOFF(){
        isOn = !isOn;
    }


    private Vector3[] CalculateVertices(){
        List<Vector3> v = new List<Vector3>();
        
        v.Add(new Vector3(0,0,0)); //0
        v.Add(new Vector3(10,0,0)); //1
        v.Add(new Vector3(0,0,-10)); //2
        v.Add(new Vector3(10,0,-10)); //3

        v.Add(new Vector3(2,0,-2)); //4
        v.Add(new Vector3(8,0,-2)); //5
        v.Add(new Vector3(8,0,-8)); //6
        v.Add(new Vector3(2,0,-8)); //7

        v.Add(new Vector3(2,-10,-2)); //8
        v.Add(new Vector3(8,-10,-2)); //9
        v.Add(new Vector3(8,-10,-8)); //10
        v.Add(new Vector3(2,-10,-8)); //11

        v.Add(new Vector3(4,-8,-4)); //12
        v.Add(new Vector3(6,-8,-4)); //13
        v.Add(new Vector3(6,-8,-6)); //14
        v.Add(new Vector3(4,-8,-6)); //15

        return v.ToArray();
    }

    private int[] CalculateTriangles(){
        int[] t = {
            //top
            5,4,0,
            1,5,0,
            6,5,1,
            3,6,1,
            7,6,3,
            2,7,3,
            4,7,2,
            0,4,2, 

            //bottom
            10,9,8,
            11,10,8,

            //bottom inner
            12,13,14,
            12,14,15, 

            //back
            0,8,9,
            0,9,1,

            //right
            1,9,10,
            1,10,3,

            //front
            2,3,10,
            2,10,11,

            //left
            0,2,11,
            0,11,8,

            //back inner
            13,12,4,
            5,13,4,
            
            //right inner
            5,6,14,
            5,6,13,

            //front inner
            7,15,14,
            7,14,6,

            //left inner
            7,4,12,
            7,12,15



        };

        return t;
    }


    }
