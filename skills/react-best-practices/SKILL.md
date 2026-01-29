---
name: react-best-practices
description: Comprehensive React and Next.js performance optimization guide. รวมแนวทางปฏิบัติที่ดีที่สุดสำหรับการพัฒนา React และ Next.js
version: 1.0.0
---

# React Best Practices - Performance Optimization

Comprehensive performance optimization guide for React and Next.js applications with 40+ rules organized by impact level.

## Key areas covered:
- **Eliminating Waterfalls** (CRITICAL): Prevent sequential async operations
- **Bundle Size Optimization** (CRITICAL): Reduce initial JavaScript payload
- **Server-Side Performance** (HIGH): Optimize RSC and data fetching
- **Client-Side Data Fetching** (MEDIUM-HIGH): Implement efficient caching
- **Re-render Optimization** (MEDIUM): Minimize unnecessary re-renders
- **Rendering Performance** (MEDIUM): Optimize browser rendering

## Quick reference

### Critical priorities

1. **Defer await until needed** - Move awaits into branches where they're used
2. **Use Promise.all()** - Parallelize independent async operations
3. **Avoid barrel imports** - Import directly from source files
4. **Dynamic imports** - Lazy-load heavy components
5. **Strategic Suspense** - Stream content while showing layout

### Common patterns

**Parallel data fetching:**
```typescript
const [user, posts, comments] = await Promise.all([
  fetchUser(),
  fetchPosts(),
  fetchComments()
])
```

**Direct imports:**
```tsx
// ❌ Loads entire library
import { Check } from 'lucide-react'

// ✅ Loads only what you need
import Check from 'lucide-react/dist/esm/icons/check'
```

**Dynamic components:**
```tsx
import dynamic from 'next/dynamic'

const MonacoEditor = dynamic(
  () => import('./monaco-editor'),
  { ssr: false }
)
```
