# 🚀 Vercel Deployment Guide - UIC Patent Portal

## 📋 Complete Deployment Settings

### 1. **Repository Setup**
- **GitHub Repository**: `https://github.com/wwwnitishsharma8146-ship-it/uicc.git`
- **Branch**: `main`
- **Auto-deploy**: Enabled

### 2. **Vercel Project Configuration**

#### Basic Settings:
```
Project Name: uic-patent-portal
Framework Preset: Other
Root Directory: ./
Node.js Version: 18.x (default)
```

#### Build Settings:
```
Build Command: (leave empty - not needed for Python)
Output Directory: (leave empty)
Install Command: pip install -r api/requirements.txt
Development Command: python api/app.py
```

### 3. **Environment Variables**

Add these in Vercel Dashboard → Settings → Environment Variables:

```bash
# Production Environment
FLASK_ENV=production
PYTHONPATH=/var/task
NODE_ENV=production

# Optional: Custom Settings
MAX_CONTENT_LENGTH=16777216
SECRET_KEY=uic-patent-portal-production-key-2026-secure
```

### 4. **Domain Configuration**

#### Default Domains:
- `https://uicc.vercel.app` (auto-generated)
- `https://uicc-git-main-wwwnitishsharma8146-ship-it.vercel.app`

#### Custom Domain Setup:
1. Go to Vercel Dashboard → Domains
2. Add custom domain: `patent.yourdomain.com`
3. Configure DNS records:
   ```
   Type: CNAME
   Name: patent
   Value: cname.vercel-dns.com
   ```

### 5. **Function Configuration**

#### Serverless Function Limits:
```json
{
  "functions": {
    "api/index.py": {
      "maxDuration": 30,        // 30 seconds max execution
      "memory": 1024,           // 1GB RAM
      "regions": ["iad1"]       // US East region
    }
  }
}
```

### 6. **Performance Settings**

#### Caching:
```json
{
  "headers": [
    {
      "source": "/api/(.*)",
      "headers": [
        {
          "key": "Cache-Control",
          "value": "s-maxage=0, max-age=0"
        }
      ]
    },
    {
      "source": "/(.*)",
      "headers": [
        {
          "key": "X-Content-Type-Options",
          "value": "nosniff"
        },
        {
          "key": "X-Frame-Options",
          "value": "DENY"
        },
        {
          "key": "X-XSS-Protection",
          "value": "1; mode=block"
        }
      ]
    }
  ]
}
```

### 7. **Deployment Commands**

#### Via Vercel CLI:
```bash
# Install Vercel CLI
npm i -g vercel

# Login to Vercel
vercel login

# Deploy to preview
vercel

# Deploy to production
vercel --prod

# Check deployment status
vercel ls
```

#### Via Git Push:
```bash
# Any push to main branch auto-deploys
git add .
git commit -m "Update application"
git push origin main
```

### 8. **Monitoring & Analytics**

#### Enable in Vercel Dashboard:
- **Analytics**: Track page views and performance
- **Speed Insights**: Monitor Core Web Vitals
- **Function Logs**: Debug serverless functions
- **Real-time Logs**: Monitor live traffic

### 9. **Security Settings**

#### CORS Configuration:
```python
CORS(app, 
     supports_credentials=True,
     origins=["https://uicc.vercel.app", "https://your-custom-domain.com"],
     allow_headers=["Content-Type", "Authorization"],
     methods=["GET", "POST", "OPTIONS"])
```

#### Security Headers:
```json
{
  "headers": [
    {
      "source": "/(.*)",
      "headers": [
        {
          "key": "Strict-Transport-Security",
          "value": "max-age=31536000; includeSubDomains"
        },
        {
          "key": "Content-Security-Policy",
          "value": "default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'"
        }
      ]
    }
  ]
}
```

### 10. **Troubleshooting**

#### Common Issues:
1. **Function Timeout**: Increase `maxDuration` in vercel.json
2. **Memory Limit**: Increase `memory` setting
3. **Import Errors**: Check Python path and dependencies
4. **CORS Issues**: Update origins in Flask-CORS config

#### Debug Commands:
```bash
# Check function logs
vercel logs

# Inspect deployment
vercel inspect [deployment-url]

# Test locally
vercel dev
```

### 11. **File Structure**
```
project/
├── api/
│   ├── index.py          # Main entry point
│   ├── app.py           # Flask application
│   └── requirements.txt  # Python dependencies
├── backend/             # Original backend (kept for reference)
├── vercel.json          # Vercel configuration
└── README.md
```

### 12. **Deployment Checklist**

- [ ] Repository connected to Vercel
- [ ] Environment variables configured
- [ ] Custom domain added (optional)
- [ ] SSL certificate enabled (automatic)
- [ ] Function limits configured
- [ ] CORS origins updated
- [ ] Analytics enabled
- [ ] Security headers configured
- [ ] Deployment tested
- [ ] Error monitoring setup

## 🎯 Quick Deploy Steps

1. **Connect Repository**: Link GitHub repo to Vercel
2. **Configure Settings**: Use settings above
3. **Set Environment Variables**: Add production variables
4. **Deploy**: Push to main branch or use Vercel CLI
5. **Test**: Verify all functionality works
6. **Monitor**: Check logs and analytics

## 📞 Support

- **Vercel Docs**: https://vercel.com/docs
- **Python Runtime**: https://vercel.com/docs/functions/serverless-functions/runtimes/python
- **Troubleshooting**: https://vercel.com/docs/functions/serverless-functions/troubleshooting