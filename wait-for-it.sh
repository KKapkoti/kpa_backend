#!/usr/bin/env bash
# wait-for-it.sh — waits for a host:port to become available

hostport="$1"
shift

host="${hostport%%:*}"
port="${hostport##*:}"

echo "Waiting for $host:$port to be ready..."

while ! nc -z "$host" "$port"; do
  sleep 1
done

echo "$host:$port is available. Starting application..."
exec "$@"
