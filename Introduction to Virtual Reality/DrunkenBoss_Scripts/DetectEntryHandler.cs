using UnityEngine;

public class DetectEntryHandler : MonoBehaviour
{
    public GameObject[] spawnboxes;
    void OnTriggerEnter(Collider other)
    {
        if (other.gameObject.CompareTag("TheBoss"))
        {
            foreach (GameObject spawnbox in spawnboxes)
            {
                spawnbox.SetActive(true);
            }
        }
        Destroy(this.gameObject);
    }
}
