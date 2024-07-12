using System.Collections;
using System.Collections.Generic;
using Unity.VisualScripting;
using UnityEngine;
using UnityEngine.AI;

public class AlienTakeDamage : MonoBehaviour
{
    Animator animator;
    NavMeshAgent agent;
    AlienPawnAnimationHandler alienPawnAnimationHandler;

    int hit = 1;
    void Start()
    {
        animator = GetComponent<Animator>();
        agent = GetComponent<NavMeshAgent>();
        alienPawnAnimationHandler = GetComponent<AlienPawnAnimationHandler>();
    }

    private void OnTriggerEnter(Collider other)
    {
        if (other.gameObject.CompareTag("Limb") || other.gameObject.CompareTag("bomb"))
        {
            if (hit == 1)
            {
                animator.SetTrigger("Death");
                agent.enabled = false;
                alienPawnAnimationHandler.enabled = false;
                StartCoroutine(Death());
                hit--;
            }
            else
            {
                hit++;
            }
        }
    }

    IEnumerator Death()
    {
        this.gameObject.GetComponent<AlienPawnAnimationHandler>().sphereCollider.enabled = false;
        this.gameObject.GetComponent<CapsuleCollider>().enabled = false;
        yield return new WaitForSeconds(3);
        DestroyImmediate(this.gameObject);
    }
}
