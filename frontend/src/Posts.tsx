import { useState, useEffect, useCallback } from 'react'
import './Posts.css'
import { mockPosts } from './mock'

export const Posts = () => {
  const [posts, setPosts] = useState(mockPosts)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  

  const loadInitialData =  useCallback(() => {
    try {
      setLoading(true)
      fetchRandomPosts()
    } catch  {
      setError('Ошибка загрузки данных')
    } finally {
      setLoading(false)
    }
  },[])

  const fetchRandomPosts = async () => {
    const response = await fetch(`${import.meta.env.VITE_API}/posts/`, {
      headers: {
        'Content-Type': 'application/json',
      },
    })
    const data = await response.json()


    setPosts(data.posts)
  }

  // Загрузка данных при монтировании
  useEffect(() => {
    loadInitialData()
  }, [loadInitialData])

  if (loading) {
    return (
      <div className="posts-container">
        <div className="loading">Загрузка данных...</div>
      </div>
    )
  }

  if (error) {
    return (
      <div className="posts-container">
        <div className="error">
          Ошибка: {error}
          <button onClick={loadInitialData} className="retry-btn">
            Попробовать снова
          </button>
        </div>
      </div>
    )
  }

  return (
    <div className="posts-container">
      <div className="posts-header">
        <h2>Посты из базы данных</h2>
      </div>

      {/* Статистика */}
      <div className="posts-stats">Найдено постов: {posts.length}</div>

      {/* Список постов */}
      <div className="posts-list">
        {posts.map(post => (
          <div key={post.id} className="post-card">
            <h3 className="post-title">{post.title}</h3>
            <div className="post-meta">
              <span className="author">👤 {post.author.name}</span>
              <span className="category">🏷️ {post.category?.name || 'Без категории'}</span>
              <span className="date">📅 {post.created_at}</span>
            </div>
            <p className="post-content">{post.content}</p>
            <div className="post-stats">
              <span className="likes">❤️ {post.likes_count}</span>
              <span className="comments">💬 {post.comments_count}</span>
              <span className="views">👁️ {post.view_count}</span>
            </div>
          </div>
        ))}
      </div>

      {posts.length === 0 && (
        <div className="no-posts">Посты не найдены. Попробуйте изменить фильтры.</div>
      )}
    </div>
  )
}
