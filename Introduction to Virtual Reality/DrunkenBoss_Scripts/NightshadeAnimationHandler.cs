using System.Collections;
using TMPro;
using UnityEngine;
using UnityEngine.AI;

public class NightshadeAnimationHandler : MonoBehaviour
{
    NavMeshAgent navMeshAgent;
    Animator animator;
    public GameObject theBossAgent;

    float nightshadeSpeed;
    // Start is called before the first frame update
    float spawnAliensCD = 1, ultimateCD = 15, uppercutCD = 1f;
    public GameObject rotator, spawnBox, nightshadeHPPanel;

    public float currentHP = 100;
    public float maxHP = 100;

    public bool isCasting = false;

    public TextMeshProUGUI HP;

    public SphereCollider sphereCollider;

    AudioSource audioSource;

    public AudioClip punch, laugh, special, death, boom;

    void OnValidate()
    {
        if (animator == null)
        {
            animator = GetComponent<Animator>();
        }

        if (navMeshAgent == null)
        {
            navMeshAgent = GetComponent<NavMeshAgent>();
        }
    }

    void Start()
    {
        navMeshAgent = GetComponent<NavMeshAgent>();
        animator = GetComponent<Animator>();
        audioSource = GetComponent<AudioSource>();
        audioSource.PlayOneShot(laugh);
    }

    // Update is called once per frame
    void Update()
    {

        if (currentHP <= 0)
        {
            animator.SetTrigger("Death");
            audioSource.PlayOneShot(death);
            navMeshAgent.speed = 0;
            PlayerPrefs.SetFloat("Death", 1);
            TheBossAnimationHandler theBossAnimationHandler = theBossAgent.GetComponent<TheBossAnimationHandler>();
            theBossAnimationHandler.enabled = false;
            NavMeshAgent theBoss = theBossAgent.GetComponent<NavMeshAgent>();
            theBoss.ResetPath();
            this.enabled = false;
        }

        if (Vector3.Distance(this.transform.position, theBossAgent.transform.position) < 20f)
            nightshadeHPPanel.SetActive(true);

        HP.text = currentHP + " / " + maxHP;

        if (currentHP <= 75f)
            ultimateCD -= Time.deltaTime;

        if (currentHP <= 50f)
            spawnAliensCD -= Time.deltaTime;

        uppercutCD -= Time.deltaTime;

        if (!isCasting)
        {
            if ((int)spawnAliensCD <= 0 && currentHP <= 30)
            {
                spawnBox.SetActive(true);
                spawnAliensCD = Mathf.Infinity;
            }
        }

        if (!isCasting)
            if ((int)ultimateCD <= 0)
            {
                rotator.transform.position = theBossAgent.transform.position + new Vector3(0, 2f, 0);
                rotator.SetActive(true);
                animator.SetTrigger("CastSpell");
                isCasting = true;
                navMeshAgent.speed = 0;
                audioSource.PlayOneShot(special);
                StartCoroutine(RemoveUltimate());
            }

        if (!isCasting)
            if ((int)uppercutCD <= 0)
                if (Vector3.Distance(theBossAgent.transform.position, this.transform.position) < 1f)
                {
                    navMeshAgent.ResetPath();
                    this.transform.LookAt(theBossAgent.transform.position);
                    animator.SetTrigger("Uppercut");
                    audioSource.PlayOneShot(punch);
                    uppercutCD = Random.Range(5, 10);
                }


        if (Vector3.Distance(this.transform.position, theBossAgent.transform.position) < 15f && Vector3.Distance(this.transform.position, theBossAgent.transform.position) > 3f)
            navMeshAgent.SetDestination(theBossAgent.transform.position);

        if (navMeshAgent.hasPath)
        {
            var dir = (navMeshAgent.steeringTarget - transform.position).normalized;
            var animDir = transform.InverseTransformDirection(dir);

            var forwardDir = Vector3.Dot(dir, transform.forward);

            if (forwardDir > 0.5f)
            {
                nightshadeSpeed = animDir.z;
            }
            else
            {
                nightshadeSpeed = 0f;
            }

            animator.SetFloat("NightShadeSpeed", nightshadeSpeed, .5f, Time.deltaTime);

            transform.rotation = Quaternion.RotateTowards(transform.rotation, Quaternion.LookRotation(dir), 300 * Time.deltaTime);

            if (Vector3.Distance(transform.position, navMeshAgent.destination) < navMeshAgent.radius) navMeshAgent.ResetPath();
        }
        else
        {
            animator.SetFloat("NightShadeSpeed", 0f, .5f, Time.deltaTime);
        }

    }

    private void OnDrawGizmos()
    {
        for (var i = 0; i < navMeshAgent.path.corners.Length - 1; i++)
        {
            Debug.DrawLine(navMeshAgent.path.corners[i], navMeshAgent.path.corners[i + 1], Color.red);
        }
    }

    IEnumerator RemoveUltimate()
    {
        yield return new WaitForSeconds(6);
        GameObject explosionCollider = rotator.transform.GetChild(0).gameObject;
        explosionCollider.SetActive(true);
        yield return new WaitForSeconds(1);
        explosionCollider.SetActive(false);
        audioSource.PlayOneShot(boom);
        yield return new WaitForSeconds(1);
        rotator.SetActive(false);
        navMeshAgent.speed = 5;
        ultimateCD = 15f;
        isCasting = false;
    }
}
