using System.Collections;
using System.Collections.Generic;
using Unity.VisualScripting;
using UnityEngine;

public class PunchBehaviour : StateMachineBehaviour
{
    TheBossAnimationHandler theBossAnimationHandler;
    // OnStateEnter is called when a transition starts and the state machine starts to evaluate this state
    override public void OnStateEnter(Animator animator, AnimatorStateInfo stateInfo, int layerIndex)
    {
        theBossAnimationHandler = animator.GetComponent<TheBossAnimationHandler>();
        if (stateInfo.IsName("Hook"))
            theBossAnimationHandler.rightHandSphereCollider.enabled = true;
        else
            theBossAnimationHandler.leftHandSphereCollider.enabled = true;
        animator.SetBool("isPunching", true);
    }

    // OnStateUpdate is called on each Update frame between OnStateEnter and OnStateExit callbacks
    //override public void OnStateUpdate(Animator animator, AnimatorStateInfo stateInfo, int layerIndex)
    //{
    //    
    //}

    // OnStateExit is called when a transition ends and the state machine finishes evaluating this state
    override public void OnStateExit(Animator animator, AnimatorStateInfo stateInfo, int layerIndex)
    {
        theBossAnimationHandler = animator.GetComponent<TheBossAnimationHandler>();
        theBossAnimationHandler.rightHandSphereCollider.enabled = false;
        theBossAnimationHandler.leftHandSphereCollider.enabled = false;
        animator.SetBool("isPunching", false);
    }

    // OnStateMove is called right after Animator.OnAnimatorMove()
    //override public void OnStateMove(Animator animator, AnimatorStateInfo stateInfo, int layerIndex)
    //{
    //    // Implement code that processes and affects root motion
    //}

    // OnStateIK is called right after Animator.OnAnimatorIK()
    //override public void OnStateIK(Animator animator, AnimatorStateInfo stateInfo, int layerIndex)
    //{
    //    // Implement code that sets up animation IK (inverse kinematics)
    //}
}
