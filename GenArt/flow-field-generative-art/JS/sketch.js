let n, noise_scale, noise_strength, particles, color

function setup() {
  createCanvas(windowWidth, windowHeight)
  noStroke()
  background(0)

  // random_uniformSeed(1)
  // noiseSeed(1)

  n = random_uniform(2000, 5000)
  noise_scale = random_uniform(10, 1000)
  noise_strength = random_uniform(1, 10)
  color = createVector(random_uniform(255), random_uniform(255), random_uniform(255))
  particles = [n]

  for (let i = 0; i < n; i++) {
    let new_pos = createVector(random_uniform(width), random_uniform(height), random_uniform(1, 5))
    let new_dir = createVector(cos(0), sin(0))
    let new_speed = random_uniform(1, 2)
    
    particles[i] = new Particle(new_pos, new_dir, new_speed);
  }
}

function draw() {
  fill(0, 10)
  rect(0, 0, windowWidth, windowHeight)
  
  for (let i = 0; i < n; i++) {
    particles[i].run()
  }
}

class Particle {
  constructor(pos, dir, speed) {
    self.pos = pos
    self.dir = dir 
    self.speed = speed
  }
  
  run() {
    let angle = noise(self.pos.x / noise_scale, self.pos.y / noise_scale, frameCount / noise_scale) * TWO_PI * noise_strength
    self.dir.x = cos(angle)
    self.dir.y = sin(angle)
    
    let vel = self.dir.copy()
    vel.mult(self.speed)
    self.pos.add(vel)
    
    if (self.pos.x <0 || self.pos.x > width || self.pos.y < 0 || self.pos.y > height) {
      self.pos.x = random_uniform(width);
      self.pos.y = random_uniform(height);
    }
    
    fill(color.z, color.y, color.z)
    ellipse(self.pos.x, self.pos.y, self.pos.z)
  }
}

function windowResized() {
  resizeCanvas(windowWidth, windowHeight)
}
