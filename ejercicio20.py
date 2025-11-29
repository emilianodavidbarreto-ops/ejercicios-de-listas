print("--- EL GRAN DESAFÍO: RED SOCIAL SIMPLIFICADA ---")
class Post:
    def _init_(self, texto, likes):
        self.texto = texto
        self.likes = likes
        
    def _repr_(self):
        return f'Post("{self.texto[:20]}...", Likes: {self.likes})'
        
posts = []

def publicar(texto, likes=0):
    """Agrega nuevos posts al inicio (los más recientes primero)."""
    nuevo_post = Post(texto, likes)
    posts.insert(0, nuevo_post)

def ordenar_por_likes():
    """Ordena posts por cantidad de likes (mayor a menor)."""
    posts.sort(key=lambda post: post.likes, reverse=True)

def eliminar_antiguos(max_posts=10):
    """Mantiene solo los últimos 10 posts (elimina los antiguos, que están al final)."""
    while len(posts) > max_posts:
        posts.pop()

def buscar_post(texto_clave):
    """Permite buscar un post específico por texto."""
    resultados = [post for post in posts if texto_clave.lower() in post.texto.lower()]
    return resultados

# Demostración
publicar("¡Hola mundo!", 50)
publicar("Qué buen día hace hoy.", 120)
publicar("Mi viaje a la montaña.", 300)

for i in range(15):
    publicar(f"Post Antiguo {i+1}", 10)
print(f"Total de posts antes de limpieza: {len(posts)}")
eliminar_antiguos(5)
print(f"Total de posts después de limpieza (máx 5): {len(posts)}")

ordenar_por_likes()
print("Posts ordenados por Likes (Top 3):", posts[:3])

busqueda = buscar_post("montaña")
print("Resultados de búsqueda 'montaña': ",busqueda)