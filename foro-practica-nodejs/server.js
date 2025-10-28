// Importa los módulos necesarios
const express = require('express');
const path = require('path');
const bodyParser = require('express').json;

// Crea una instancia de la aplicación Express
const app = express();
// Puerto en el que el servidor escuchará (toma del entorno o por defecto 3000)
const PORT = process.env.PORT || 3000;

// Sirve archivos estáticos del frontend desde /public
app.use(express.static(path.join(__dirname, 'public')));
app.use(bodyParser());

// Importa la lógica para la gestión de posts (CRUD en posts.json)
const db = require('./db');

// Ruta GET para obtener todos los posts actuales desde la memoria (rápido)
app.get('/api/posts', (req, res) => {
  res.json(db.getAll());
});

// Ruta POST para crear un nuevo post. Valida la entrada, crea el objeto post y lo guarda.
app.post('/api/posts', async (req, res) => {
  const { text, nametag, avatarColor } = req.body;
  // Validamos que el texto no esté vacío
  if (!text || typeof text !== 'string' || text.trim().length === 0) {
    return res.status(400).json({ error: 'Post text is required' });
  }
  // Calcula el próximo id numérico
  const posts = db.getAll() || [];
  const numericIds = posts
    .map(p => Number(p.id))
    .filter(n => Number.isInteger(n) && n >= 0);
  const id = numericIds.length ? Math.max(...numericIds) + 1 : 0;

  // Crea el nuevo post
  const post = {
    id, // id secuencial numérico: 0, 1, 2, ...
    text: text.trim(),
    nametag: nametag || 'Anon',
    avatarColor: avatarColor || '#6c757d',
    createdAt: new Date().toISOString(),
    review: 0
  };
  // Guarda el nuevo post en la base de datos
  await db.add(post);
  res.status(201).json(post);
});

// Ruta DELETE para eliminar un post mediante su id
app.delete('/api/posts/:id', async (req, res) => {
  const id = Number(req.params.id);
  // Elimina el post señalado y responde según el resultado
  const ok = await db.remove(id);
  if (!ok) return res.status(404).json({ error: 'Post not found' });
  return res.status(204).end();
});

// Ruta PATCH para modificar parcialmente un post mediante su id
app.patch('/api/posts/:id', async (req, res) => {
  const id = Number(req.params.id);
  // Intenta actualizar el post y responde si existe o no
  const updated = await db.update(id, req.body);
  if (!updated) return res.status(404).json({ error: 'Post not found' });
  return res.json(updated);
});

// Ruta para autenticar usuarios (simple, revisa users.json en carpeta data)
const fs = require('fs').promises;
const USERS_FILE = path.join(__dirname, 'data', 'users.json');
app.post('/api/login', async (req, res) => {
  const { username, password } = req.body;
  if(!username || !password)
    return res.status(400).json({ error: 'Faltan datos' });
  try {
    const raw = await fs.readFile(USERS_FILE, 'utf8');
    const users = JSON.parse(raw);
    const found = users.find(u => u.username === username && u.password === password);
    if(found) {
      // Éxito (no token, solo demo)
      return res.json({ ok: true, username: found.username });
    } else {
      return res.status(401).json({ error: 'Usuario o contraseña incorrectos' });
    }
  } catch(err) {
    return res.status(500).json({ error: 'Error al procesar usuarios' });
  }
});

// Inicializa la base de datos y arranca el servidor
(async () => {
  try{
    // Carga los posts a memoria antes de aceptar peticiones
    await db.init();
    app.listen(PORT, () => {
      console.log(`Server listening on http://localhost:${PORT}`);
    });
  }catch(err){
    // Si falla la inicialización, muestra error y termina
    console.error('Failed to initialize data storage:', err);
    process.exit(1);
  }
})();
