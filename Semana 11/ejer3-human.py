class Head:
    def __init__(self):
        pass

class Hand:
    def __init__(self):
        pass

class Arm:
    def __init__(self, hand):
        self.hand = hand

class Body:
    def __init__(self, head, left_arm, right_arm):
        self.head = head
        self.left_arm = left_arm
        self.right_arm = right_arm

class Feet:
    def __init__(self):
        pass

class Leg:
    def __init__(self, foot):
        self.foot = foot

class Human:
    def __init__(self, body, left_leg, right_leg):
        self.body = body
        self.left_leg = left_leg
        self.right_leg = right_leg

def create_human():
    head = Head()
    left_hand = Hand()
    right_hand = Hand()
    left_arm = Arm(left_hand)
    right_arm = Arm(right_hand)
    body = Body(head, left_arm, right_arm)
    left_foot = Feet()
    right_foot = Feet()
    left_leg = Leg(left_foot)
    right_leg = Leg(right_foot)
    human = Human(body, left_leg, right_leg)
    return human

if __name__ == "__main__":
    human = create_human()
    print("Human created with body parts:")
    print(f"Head: {human.body.head}")   
    print(f"Left Arm: {human.body.left_arm}")
    print(f"Right Arm: {human.body.right_arm}")
    print(f"Left Leg: {human.left_leg}")
    print(f"Right Leg: {human.right_leg}")
    print(f"Left Hand: {human.body.left_arm.hand}")
    print(f"Right Hand: {human.body.right_arm.hand}")
    print(f"Left Foot: {human.left_leg.foot}")
    print(f"Right Foot: {human.right_leg.foot}")
    print("Human creation complete.")