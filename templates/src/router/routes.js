
const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      {
        path: '',
        name: 'index',
        component: () => import('pages/Index.vue')
      },
      {
        path: 'bbs',
        name: 'bbs',
        component: () => import('pages/bbs/home.vue'),
        children: [
          // {
          //   path: 'outbounddashboard',
          //   name: 'outbounddashboard',
          //   component: () => import('pages/dashboard/outbound.vue')
          // },
        ]
      },
    ]
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/Error404.vue')
  }
]

export default routes
