using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class GPUComputeTerrain : MonoBehaviour
{

    [SerializeField] int resX = 200, resY = 200;

    [SerializeField] Transform lightPos, cameraPos;

    MeshFilter mf;
    MeshRenderer mr; 

    Material mat;

    float y;

    [Range(0.1f, 10.0f)] [SerializeField] float intensity;
    [Range(0.001f, 0.01f)] [SerializeField] float sunSpeed = 0.001f;

    public Color ambientColor, specularColor, diffuseColor;

    bool isOn;


    void Awake(){

        isOn = true;

        mf = GetComponent<MeshFilter>();
        mr = GetComponent<MeshRenderer>();

        Mesh m = new Mesh();
        m.vertices = getVertices();
        m.triangles = getTriangles();
        m.Optimize();
        m.RecalculateNormals();

        mf.mesh = m;

        mat = mr.material;
        
    }


    void Update()
    {   
        
        if(isOn){
            mat.SetFloat("isOn", 1f);
        }
        else{
            mat.SetFloat("isOn", 2f);
        }
        
        lightPos.position = RotationMatrix("z", sunSpeed).MultiplyVector(RotationMatrix("y", sunSpeed * -1f).MultiplyVector(lightPos.position)) ;
        mat.SetVector("lightPos", lightPos.position);
        mat.SetVector("cameraPos", cameraPos.position);
        mat.SetVector("ambientColor", ambientColor);
        mat.SetVector("diffuseColor", diffuseColor);
        mat.SetVector("specularColor", specularColor);
        mat.SetFloat("_Intensity", intensity);
    }

    public void switchONOFF(){
        isOn = !isOn;
    }

    private Vector3[] getVertices()
    {
        List<Vector3> vertices = new List<Vector3>();
        
        for (int i = 0; i < resX; i++)
            for (int j = 0; j < resY; j++){
                y = 0;
                y = Mathf.PerlinNoise(i * 0.3f, j * 0.5f) * 2f; //https://docs.unity3d.com/ScriptReference/Mathf.PerlinNoise.html
                vertices.Add(new Vector3(i - resX/2, 0, -j + resY/2));
            }
                

        return vertices.ToArray();
    }


    private int[] getTriangles()
    {
        List<int> indexToReturn = new List<int>();

        for (int i = 0; i < resX - 1; i++)
        {
            for (int j = 0; j < resY - 1; j++)
            {
                indexToReturn.Add(i + ((j + 1) * resX));
                indexToReturn.Add(i + (j * resX) + 1);
                indexToReturn.Add(i + (j * resX));

                indexToReturn.Add(i + ((j + 1) * resX));
                indexToReturn.Add(i + ((j + 1) * resX) + 1);
                indexToReturn.Add(i + (j * resX) + 1);
                
            }
        }

        return indexToReturn.ToArray();
    }

    Matrix4x4 RotationMatrix(string axis, float angle){

        if (axis == "x"){
            return new Matrix4x4(
            new Vector4(1, 0, 0, 0),
            new Vector4(0, Mathf.Cos(angle), -Mathf.Sin(angle), 0),
            new Vector4(0, Mathf.Sin(angle), Mathf.Cos(angle), 0),
            new Vector4(0, 0, 0, 1)
        );
        }

        if (axis == "y"){
            return new Matrix4x4(
            new Vector4(Mathf.Cos(angle), 0, Mathf.Sin(angle), 0),
            new Vector4(0, 1, 0, 0),
            new Vector4(-Mathf.Sin(angle), 0, Mathf.Cos(angle), 0),
            new Vector4(0, 0, 0, 1)
        );
        }

        if (axis == "z"){
            return new Matrix4x4(
            new Vector4(Mathf.Cos(angle), -Mathf.Sin(angle), 0, 0),
            new Vector4(Mathf.Sin(angle), Mathf.Cos(angle), 0, 0),
            new Vector4(0, 0, 1, 0),
            new Vector4(0, 0, 0, 1)
        );
        }
        else return Matrix4x4.identity;
        
    }

    Matrix4x4 TranslationMatrix(Vector3 newPos){
        return new Matrix4x4(
            new Vector4(1,0,0,newPos.x),
            new Vector4(0,1,0,newPos.y),
            new Vector4(0,0,1,newPos.z),
            new Vector4(0,0,0,1)
        );
    }

    Matrix4x4 ScalingMatrix(Vector3 s){
        return new Matrix4x4(
            new Vector4(s.x, 0, 0, 0),
            new Vector4(0, s.y, 0, 0),
            new Vector4(0, 0, s.z, 0),
            new Vector4(0, 0, 0, 1)
        );
    }


}
