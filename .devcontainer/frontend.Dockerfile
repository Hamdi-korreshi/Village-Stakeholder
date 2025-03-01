FROM node:18

WORKDIR /workspace/frontend

COPY frontend/package.json frontend/package-lock.json ./

RUN npm install --include=dev

EXPOSE 5173

CMD ["npm", "run", "dev", "--", "--host"]
