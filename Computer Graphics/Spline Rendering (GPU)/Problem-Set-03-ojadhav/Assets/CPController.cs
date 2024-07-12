using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

namespace PS03{
    public class CPController : MonoBehaviour
    {
        [SerializeField] GameObject[] controlPoints;
        [SerializeField] GameObject[] splineSegments;
        [SerializeField] GameObject reset;
        public Collider2D[] colliders;
        public float radius;
        int counter = 0;
        int splineCounter = 0;
        SplineSegmentGPUComputeTaskC sc;
        

        private Camera myMainCamera;
        private Vector2 myMouseStartWorldPosition;

        public void resetScene(){
            SceneManager.LoadScene("MultipleSegmentGPUSpline_TaskC");
        }
        
        private void Awake() {
            // obtain the main Camera used in the scene:
            myMainCamera = Camera.main;
        }

        void Update(){
            if(Input.GetMouseButtonDown(0)){
                if(counter % 3 == 0 && counter != 0){
                    sc = splineSegments[splineCounter].GetComponent<SplineSegmentGPUComputeTaskC>();
                    sc.enabled = true;
                    splineCounter += 1;
                }
                if(counter >= controlPoints.Length){
                    reset.SetActive(true);
                }
                else{
                    Vector2 lMousePosition = Input.mousePosition;
                    Vector2 lMouseCurrentWorldPosition = myMainCamera.ScreenToWorldPoint(lMousePosition) ;
                    if(!invalidPos(lMouseCurrentWorldPosition)){
                        controlPoints[counter].transform.position = lMouseCurrentWorldPosition;
                        controlPoints[counter].SetActive(true);
                        counter += 1;
                    }
                    
                }
            }  
        }

        bool invalidPos(Vector3 pos){
            colliders = Physics2D.OverlapCircleAll(pos, radius);

            for(int i = 0; i < colliders.Length; i++){
                Vector3 center = colliders[i].bounds.center;
                float width = colliders[i].bounds.extents.x;
                float height = colliders[i].bounds.extents.y;

                float l = center.x - width;
                float r = center.x + width;
                float low = center.y - height;
                float up = center.y + height;

                if(pos.x >= l && pos.x <= r){
                    if(pos.y >= low && pos.y <= up){
                        return true;
                    }
                }
            }
            return false;
        }

    }
}

