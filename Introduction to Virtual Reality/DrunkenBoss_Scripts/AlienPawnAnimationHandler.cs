using System;
using UnityEngine;
using UnityEngine.AI;

public class AlienPawnAnimationHandler : MonoBehaviour
{
    [SerializeField]
    NavMeshAgent agent;
    [SerializeField]
    GameObject theBossAgent;
    [SerializeField]
    Animator animator;

    float alienSpeed;

    public SphereCollider sphereCollider;


    // Start is called before the first frame update
    void Start()
    {
    }

    // Update is called once per frame
    void Update()
    {
        // Set a path only if TheBoss is close
        if (Vector3.Distance(this.transform.position, theBossAgent.transform.position) < 20f && Vector3.Distance(this.transform.position, theBossAgent.transform.position) > 1.5f)
            agent.SetDestination(theBossAgent.transform.position);

        // Punch if close
        if (Vector3.Distance(this.transform.position, theBossAgent.transform.position) < 1.5f)
        {
            this.transform.LookAt(theBossAgent.transform);
            agent.ResetPath();
            alienSpeed = 0f;
            animator.SetTrigger("Punch");
        }

        // Only move is Path is available
        if (agent.hasPath)
        {
            // Get the global direction towards the destination
            Vector3 direction = (agent.steeringTarget - transform.position).normalized;
            // Convert into local direction
            Vector3 localDirection = transform.InverseTransformDirection(direction);

            float forwardDir = Vector3.Dot(direction, transform.forward);

            if (forwardDir > 0.5f)
            {
                alienSpeed = localDirection.z;
            }
            else
            {
                alienSpeed = 0f;
            }

            animator.SetFloat("AlienSpeed", alienSpeed, .2f, Time.deltaTime);

            // Smooth Rotation
            transform.rotation = Quaternion.RotateTowards(transform.rotation, Quaternion.LookRotation(direction), 500 * Time.deltaTime);

            if (Vector3.Distance(transform.position, agent.destination) < agent.radius) agent.ResetPath();
        }
        else
        {
            animator.SetFloat("AlienSpeed", 0f, .5f, Time.deltaTime);
        }
    }

    private void OnDrawGizmos()
    {
        for (var i = 0; i < agent.path.corners.Length - 1; i++)
        {
            Debug.DrawLine(agent.path.corners[i], agent.path.corners[i + 1], Color.blue);
        }
    }
}
