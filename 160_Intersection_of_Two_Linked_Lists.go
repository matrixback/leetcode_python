/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func getIntersectionNode(headA, headB *ListNode) *ListNode {
    a_length := getLength(headA)
    b_length := getLength(headB)
    if a_length > b_length {
        steps := a_length - b_length
        for steps > 0 {
            headA = headA.Next
            steps--
        }
    } else {
        steps := b_length - a_length
        for steps > 0 {
            headB = headB.Next
            steps--
        }
    }

    for {
        if headA == headB {
            return headA
        } else {
            headA = headA.Next
            headB = headB.Next
        }
    }

    return nil
}

func getLength(head *ListNode) (length int) {
    length = 0
    for head != nil {
        length++
        head = head.Next
    }
    return
}
