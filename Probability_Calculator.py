import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)  # Add each color to the contents list based on count

    def draw(self, num_balls):
        if num_balls >= len(self.contents):
            drawn_balls = self.contents[:]  # Draw all balls if more are drawn than available
            self.contents.clear()  # Clear the contents since all balls are drawn
            return drawn_balls
        
        drawn_balls = random.sample(self.contents, num_balls)  # Draw 'num_balls' without replacement
        for ball in drawn_balls:
            self.contents.remove(ball)  # Remove drawn balls from contents
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_count = 0

    for _ in range(num_experiments):
        # Create a copy of the hat for each experiment
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)  # Draw balls from the hat

        # Check if the drawn balls meet the expected criteria
        drawn_counts = {color: drawn_balls.count(color) for color in expected_balls}
        if all(drawn_counts.get(color, 0) >= count for color, count in expected_balls.items()):
            success_count += 1  # Count successful experiments

    return success_count / num_experiments  # Calculate the probability

# Example usage
if __name__ == "__main__":
    hat = Hat(black=7, red=9, green=11)
    probability = experiment(hat=hat,
                             expected_balls={'red': 2, 'green': 1},
                             num_balls_drawn=5,
                             num_experiments=2000)
    print(probability)  # Output will vary due to randomness
