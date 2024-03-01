import { test } from 'vitest'

import { describe, expect, it } from 'vitest';
import { mountSuspended} from '@nuxt/test-utils/runtime'
import App from '@/app.vue';

describe('app.vue',  () => {
    it('renders correctly', async () => {
      const component = await mountSuspended(App); 
      expect(component.html()).toContain('Welcome to Nuxt');
    });
  });