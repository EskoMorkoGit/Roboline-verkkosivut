import { defineConfig } from 'vite';

export default defineConfig({
  root: './',
  build: {
    rollupOptions: {
      input: {
        main: 'index.html',
        ymmarryksentie: 'ymmarryksentie.html',
        mockup: 'mockup-studio.html',
      },
    },
  },
  server: {
    open: true,
  },
});
