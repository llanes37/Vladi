// Módulo para la gestión de almacenamiento local de posts en formato JSON
const fs = require('fs').promises;
const path = require('path');

// Directorio y fichero donde se persisten los posts en formato JSON
const DATA_DIR = path.join(__dirname, 'data');
const FILE = path.join(DATA_DIR, 'posts.json');

// Variable global en memoria que almacena los posts cargados
let posts = [];

// Asegura que el directorio de datos existe antes de operar con archivos
async function ensureDir(){
  await fs.mkdir(DATA_DIR, { recursive: true });
}

// Lee el fichero de posts y garantiza un array como resultado. Si no existe, regresa []
async function readFileSafe(){
  try{
    await ensureDir(); // Asegura carpeta de datos
    const raw = await fs.readFile(FILE, 'utf8');
    const parsed = JSON.parse(raw);
    return Array.isArray(parsed) ? parsed : [];
  }catch(err){
    // Si no existe el fichero, consideramos la base de datos vacía.
    if(err.code === 'ENOENT') return [];
    // Re-lanzar otros errores para que el llamador los gestione.
    throw err;
  }
}

// Escribe el fichero JSON de manera segura usando un temporal. Así evitamos corrupciones
async function writeFileAtomic(data){
  await ensureDir();
  const tmp = FILE + '.tmp';
  await fs.writeFile(tmp, JSON.stringify(data, null, 2), 'utf8');
  await fs.rename(tmp, FILE);
}

// API pública del módulo - expone las operaciones principales para manejar posts
module.exports = {
  // Inicializa la caché de memoria leyendo el fichero de posts
  async init(){
    posts = await readFileSafe();
    return posts;
  },

  // Devuelve todos los posts cargados en memoria (sin leer disco)
  getAll(){
    return posts;
  },

  // Añade un nuevo post, lo inserta al principio de la lista (más recientes) y guarda
  async add(post){
    posts.unshift(post); // Inserta al inicio
    posts = posts.slice(0, 100); // Limita a 100 elementos para no crecer indefinidamente
    await writeFileAtomic(posts); // Persiste cambios
    return post;
  },

  // Actualiza un post existente por id, acepta un objeto con los cambios parciales
  async update(id, patch){
    const idx = posts.findIndex(p => p.id === id);
    if(idx === -1) return null; // No encontrado
    // Solo actualizamos los campos permitidos
    if(patch.text && typeof patch.text === 'string' && patch.text.trim().length > 0) posts[idx].text = patch.text.trim();
    if(patch.nametag) posts[idx].nametag = patch.nametag;
    if(patch.avatarColor) posts[idx].avatarColor = patch.avatarColor;
    if(typeof patch.review === 'number' && patch.review >= 0 && patch.review <= 10) posts[idx].review = patch.review;
    posts[idx].createdAt = new Date().toISOString(); // Marca la actualización
    await writeFileAtomic(posts);
    return posts[idx];
  },

  // Elimina un post por id, devuelve true si se eliminó y persiste cambios
  async remove(id){
    const before = posts.length;
    posts = posts.filter(p => p.id !== id);
    if(posts.length === before) return false; // No eliminado
    await writeFileAtomic(posts);
    return true;
  }
};
