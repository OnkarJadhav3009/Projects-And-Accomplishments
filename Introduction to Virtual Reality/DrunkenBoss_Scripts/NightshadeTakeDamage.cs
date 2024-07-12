using UnityEngine;
using UnityEngine.AI;

public class NightshadeTakeDamage : MonoBehaviour
{
    NavMeshAgent navMeshAgent;
    Animator animator;
    NightshadeAnimationHandler nightshadeAnimationHandler;

    void Start()
    {
        navMeshAgent = GetComponent<NavMeshAgent>();
        animator = GetComponent<Animator>();
        nightshadeAnimationHandler = GetComponent<NightshadeAnimationHandler>();
    }

    int hit = 1;

    void OnTriggerEnter(Collider other)
    {
        if (other.gameObject.CompareTag("Limb"))
        {
            if (hit == 1)
            {
                nightshadeAnimationHandler.currentHP -= Random.Range(5, 10);
                animator.SetTrigger("TakeDamage");
                hit--;
            }
            else
            {
                hit++;
            }
        }

        if (other.gameObject.CompareTag("bomb"))
        {

            nightshadeAnimationHandler.currentHP -= Random.Range(20, 30);
            animator.SetTrigger("TakeDamage");

        }
    }
}
