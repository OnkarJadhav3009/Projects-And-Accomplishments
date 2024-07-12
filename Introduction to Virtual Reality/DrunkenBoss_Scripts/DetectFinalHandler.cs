using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DetectFinalHandler : MonoBehaviour
{
    public GameObject Nightshade;
    public GameObject BGAudio;
    public GameObject FinalBossAudio;

    void OnTriggerEnter(Collider other)
    {
        if (other.gameObject.CompareTag("TheBoss"))
        {
            BGAudio.SetActive(false);
            FinalBossAudio.SetActive(true);
            Nightshade.SetActive(true);
        }
    }
}
