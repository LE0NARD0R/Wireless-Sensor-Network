import { createRouter, createWebHistory } from 'vue-router'
import MeditionsView from '../views/MeditionsView.vue'
import ChartView from '../views/ChartView.vue'
import InstantView from '../views/InstantView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'instant',
      component: InstantView
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/charts',
      name: 'charts',
      component: ChartView
    },
    {
      path: '/meditions',
      name: 'meditions',
      component: MeditionsView
    },
  ]
})

export default router
