using System.Collections;
using System.Globalization;
using TMPro;
using Unity.VisualScripting;
using UnityEngine;
using UnityEngine.AI;
using UnityEngine.UI;

public class TheBossAnimationHandler : MonoBehaviour
{
    [SerializeField]
    NavMeshAgent agent;
    Animator animator;

    public float currentHP = 100;
    float maxHP = 100;

    public int numberOfPunches = 2;
    int punchIndex = 0;

    public SphereCollider rightHandSphereCollider;
    public SphereCollider leftHandSphereCollider;

    float powerUpCD = 10f;
    float specialCD = 20f;
    float potionCD = 20f;

    public GameObject powerUp;
    public GameObject explosion;
    public GameObject NightShade;


    public TextMeshProUGUI powerUpCDText;
    public TextMeshProUGUI specialCDText;
    public TextMeshProUGUI Health;
    public TextMeshProUGUI potionCDText;

    float horizontalValue, verticalValue;
    bool isPunching = false, isRolling = false, isMoving;

    public AudioClip PunchSound, RollSound, ExplodeSound, DeathSound;
    AudioSource audioSource;

    // Start is called before the first frame update
    void Start()
    {
        agent = GetComponent<NavMeshAgent>();
        animator = GetComponent<Animator>();
        audioSource = GetComponent<AudioSource>();

    }

    // Update is called once per frame
    void Update()
    {
        GetParams();

        Health.text = "HP  " + (int)currentHP + " /" + maxHP;

        CheckCooldown();

        if (currentHP <= 0)
        {
            audioSource.PlayOneShot(DeathSound);
            animator.SetTrigger("Death");
            this.enabled = false;
            NightshadeAnimationHandler nightshadeAnimationHandler = NightShade.GetComponent<NightshadeAnimationHandler>();
            PlayerPrefs.SetFloat("Death", 1);
            nightshadeAnimationHandler.enabled = false;
        }

        if (Input.GetKeyDown(KeyCode.Q))
        {
            Punch();
        }

        if (Input.GetKeyDown(KeyCode.Space))
        {
            Roll();
        }

        if ((int)potionCD <= 0)
            if (Input.GetKeyDown(KeyCode.H))
            {
                currentHP += 20f;
                if (currentHP > maxHP)
                {
                    currentHP = maxHP;
                }
                potionCD = 20f;
            }

        if (Input.GetKeyDown(KeyCode.E) && powerUpCD <= 0f)
        {
            powerUp.gameObject.SetActive(true);
            animator.SetBool("isFrenzy", true);
            StartCoroutine(RemovePowerUp());
        }

        if (Input.GetKeyDown(KeyCode.R) && specialCD <= 0f)
        {
            explosion.transform.position = this.transform.position + (this.transform.forward * 5);
            explosion.SetActive(true);
            audioSource.PlayOneShot(ExplodeSound);
            StartCoroutine(RemoveSpecial());
        }

        if (agent.hasPath)
        {

            Vector3 direction = (agent.steeringTarget - transform.position).normalized;
            Vector3 localDirection = transform.InverseTransformDirection(direction); // local space dir
            float forwardDir = Vector3.Dot(direction, transform.forward);

            if (forwardDir > 0.5f)
            {
                horizontalValue = localDirection.x;
                verticalValue = localDirection.z;
            }
            else
            {
                horizontalValue = 0f;
                verticalValue = 0f;
            }

            animator.SetFloat("Horizontal", horizontalValue, .5f, Time.deltaTime);
            animator.SetFloat("Vertical", verticalValue, .5f, Time.deltaTime);
            animator.SetBool("isMoving", true);

            transform.rotation = Quaternion.RotateTowards(transform.rotation, Quaternion.LookRotation(direction), 500 * Time.deltaTime);

            if (Vector3.Distance(transform.position, agent.destination) < agent.radius) agent.ResetPath();
        }
        else
        {
            animator.SetFloat("Horizontal", 0, 0.5f, Time.deltaTime);
            animator.SetFloat("Vertical", 0, 0.5f, Time.deltaTime);
            animator.SetBool("isMoving", false);
        }


        if (Input.GetMouseButton(0))
        {
            Ray ray = Camera.main.ScreenPointToRay(Input.mousePosition);
            RaycastHit hit;
            if (Physics.Raycast(ray.origin, ray.direction, out hit, Mathf.Infinity))
            {
                agent.SetDestination(hit.point);
            }
        }

    }

    private void CheckCooldown()
    {
        powerUpCD -= Time.deltaTime;
        specialCD -= Time.deltaTime;
        potionCD -= Time.deltaTime;


        if (powerUpCD <= 0f)
        {
            powerUpCDText.text = "Frenzy";
            powerUpCDText.color = Color.green;
        }
        else
        {
            powerUpCDText.text = (int)powerUpCD + "";
            powerUpCDText.color = Color.red;
        }

        if (specialCD <= 0f)
        {
            specialCDText.text = "Boom";
            specialCDText.color = Color.green;
        }
        else
        {
            specialCDText.text = (int)specialCD + "";
            specialCDText.color = Color.red;
        }

        if (potionCD <= 0f)
        {
            potionCDText.text = "Potion";
            potionCDText.color = Color.green;
        }
        else
        {
            potionCDText.text = (int)potionCD + "";
            potionCDText.color = Color.red;
        }

    }

    private void GetParams()
    {
        isPunching = animator.GetBool("isPunching");
        isMoving = animator.GetBool("isMoving");
        isRolling = animator.GetBool("isRolling");
    }

    private void OnDrawGizmos()
    {
        for (var i = 0; i < agent.path.corners.Length - 1; i++)
        {
            Debug.DrawLine(agent.path.corners[i], agent.path.corners[i + 1], Color.blue);
        }
    }

    void Punch()
    {
        if (!isPunching)
        {
            audioSource.PlayOneShot(PunchSound);
            agent.ResetPath();
            if (Vector3.Distance(NightShade.transform.position, this.transform.position) < 2f)
                transform.LookAt(NightShade.transform.position);
            animator.SetTrigger("Punch");
            punchIndex++;
            animator.SetInteger("PunchIndex", punchIndex % numberOfPunches);
        }
    }

    void Roll()
    {
        if ((!isRolling && isMoving) || isPunching)
        {
            audioSource.PlayOneShot(RollSound);
            animator.SetTrigger("Roll");
        }
    }

    IEnumerator RemovePowerUp()
    {
        yield return new WaitForSeconds(6);
        powerUp.gameObject.SetActive(false);
        animator.SetBool("isFrenzy", false);
        powerUpCD = 10f;
    }
    IEnumerator RemoveSpecial()
    {
        yield return new WaitForSeconds(2);
        explosion.SetActive(false);
        specialCD = 20f;
    }

}
