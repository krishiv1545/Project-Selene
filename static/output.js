const filePath = document.getElementById("string").textContent;
console.log(filePath);

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(
  75,
  window.innerWidth / window.innerHeight,
  0.1,
  1000
);

const renderer = new THREE.WebGLRenderer({
  canvas: document.getElementById("moonCanvas"),
  antialias: true,
});
renderer.setSize(window.innerWidth, window.innerHeight);

camera.position.z = 5;

const light = new THREE.DirectionalLight(0xf6f1d5, 1); //0xf6f1d5 0xff00f2
light.position.set(-5, 11.495, -4.91).normalize(); //5,7.5,-10
scene.add(light);

const ambientLight = new THREE.AmbientLight(0x404040);
scene.add(ambientLight);

//HELPERSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSs
/* const axesHelper = new THREE.AxesHelper(5);
scene.add(axesHelper); */
/* const lightHelper = new THREE.DirectionalLightHelper(light, 500);
scene.add(lightHelper); */

const loader = new THREE.OBJLoader();
loader.load(
  filePath,
  function (object) {
    loadedObject = object;

    scene.add(loadedObject);
    loadedObject.position.y = 0;
    loadedObject.scale.set(0.18, 0.18, 0.18);
    loadedObject.rotation.x -= Math.PI / 3;
  },

  function (xhr) {
    console.log((xhr.loaded / xhr.total) * 100 + "% loaded");
  },
  function (error) {
    console.error("An error occurred while loading the OBJ file:", error);
  }
);

const controls = new THREE.OrbitControls(camera, renderer.domElement);
controls.update();

function animate() {
  requestAnimationFrame(animate);

  if (loadedObject) {
    loadedObject.rotation.z += 1 / 1000;
  }
  renderer.render(scene, camera);
}

animate();
