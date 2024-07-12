using UnityEngine;
using UnityEngine.AI;

public class TheBossTakeDamage : MonoBehaviour
{

    Animator animator;
    NavMeshAgent agent;
    TheBossAnimationHandler theBossAnimationHandler;

    AudioSource audioSource;
    public AudioClip TakeHit;

    public int hit = 1;
    // Start is called before the first frame update
    void Start()
    {
        agent = GetComponent<NavMeshAgent>();
        animator = GetComponent<Animator>();
        theBossAnimationHandler = GetComponent<TheBossAnimationHandler>();
        audioSource = GetComponent<AudioSource>();
    }

    // Update is called once per frame
    void Update()
    {

    }

    private void OnTriggerEnter(Collider other)
    {
        if (other.gameObject.CompareTag("zombie"))
        {
            if (hit == 1)
            {
                audioSource.PlayOneShot(TakeHit);
                theBossAnimationHandler.currentHP -= 1f;
                hit--;
            }
            else
            {
                hit++;
            }
        }

        if (other.gameObject.CompareTag("nightshadeLimb"))
        {
            if (hit == 1)
            {
                theBossAnimationHandler.currentHP -= Random.Range(10, 20);
                audioSource.PlayOneShot(TakeHit);
                animator.SetTrigger("TakeDamage");
                hit--;
            }
            else
            {
                hit++;
            }
        }
    }

    private void OnTriggerStay(Collider other)
    {
        if (other.gameObject.CompareTag("ultimate"))
        {
            theBossAnimationHandler.currentHP -= Time.deltaTime;
        }

        if (other.gameObject.CompareTag("ultimateExplosion"))
        {
            theBossAnimationHandler.currentHP -= 30f * Time.deltaTime;
        }

    }
}
