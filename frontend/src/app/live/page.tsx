'use client';
import { useEffect, useState, useRef } from 'react';
import { Card, CardContent, Typography, List, ListItem, ListItemText, ListItemAvatar, Avatar } from '@mui/material';
import { Warning, CheckCircle } from '@mui/icons-material';
import io from 'socket.io-client';

export default function LiveMonitor() {
    const [logs, setLogs] = useState<any[]>([]);
    const videoRef = useRef<HTMLVideoElement>(null);

    useEffect(() => {
        // Start camera stream for demo purpose (frontend webcam)
        // In production, this would be an RTSP stream (HLS/WebRTC) from the server
        if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
            navigator.mediaDevices.getUserMedia({ video: true }).then(stream => {
                if (videoRef.current) {
                    videoRef.current.srcObject = stream;
                }
            }).catch(err => console.error(err));
        }

        const socket = io('http://localhost:8000', { path: '/ws/alerts' });
        socket.on('ALERT_NEW', (message: any) => {
            const data = JSON.parse(message).data;
            setLogs(prev => [data, ...prev].slice(0, 20)); // Keep last 20
        });

        return () => {
            socket.disconnect();
            // Stop tracked stream
        };
    }, []);

    return (
        <div className="p-8 bg-slate-900 min-h-screen text-slate-100">
            <h1 className="text-3xl font-bold mb-6">Live Security Monitor</h1>

            <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
                {/* Video Feed Section */}
                <div className="lg:col-span-2 space-y-4">
                    <Card className="bg-black border-slate-700">
                        <div className="relative aspect-video bg-black flex items-center justify-center overflow-hidden">
                            <video ref={videoRef} autoPlay playsInline muted className="w-full h-full object-cover" />
                            <div className="absolute top-4 left-4 bg-red-600 px-2 py-1 rounded text-xs animate-pulse font-bold">LIVE</div>
                            <div className="absolute bottom-4 left-4 text-xs bg-black/50 px-2 py-1">Camera 01 - Main Entrance</div>
                        </div>
                    </Card>
                    <div className="grid grid-cols-2 gap-4">
                        <div className="bg-slate-800 p-4 rounded text-center cursor-pointer hover:bg-slate-700 border border-slate-600">
                            <Typography variant="h6">Camera 02</Typography>
                            <Typography variant="caption" color="textSecondary">Corridor A</Typography>
                        </div>
                        <div className="bg-slate-800 p-4 rounded text-center cursor-pointer hover:bg-slate-700 border border-slate-600">
                            <Typography variant="h6">Camera 03</Typography>
                            <Typography variant="caption" color="textSecondary">Playground</Typography>
                        </div>
                    </div>
                </div>

                {/* Live Logs Section */}
                <div className="bg-slate-800 rounded-lg p-4 border border-slate-700 h-[600px] overflow-y-auto">
                    <Typography variant="h5" className="mb-4 sticky top-0 bg-slate-800 pb-2 border-b border-slate-700">Real-time Event Log</Typography>
                    <List>
                        {logs.length === 0 && <Typography color="textSecondary" align="center">Waiting for events...</Typography>}
                        {logs.map((log, idx) => (
                            <ListItem key={idx} className="bg-slate-700/50 mb-2 rounded border border-slate-600">
                                <ListItemAvatar>
                                    <Avatar src={`http://localhost:8000/${log.snapshot}`} variant="rounded">
                                        {log.type === 'STRANGER_DETECTED' ? <Warning color="error" /> : <CheckCircle color="success" />}
                                    </Avatar>
                                </ListItemAvatar>
                                <ListItemText
                                    primary={<span className={log.type === 'STRANGER_DETECTED' ? 'text-red-400 font-bold' : 'text-blue-300'}>{log.type.replace('_', ' ')}</span>}
                                    secondary={<span className="text-slate-400">{log.location} • {new Date(log.timestamp).toLocaleTimeString()}</span>}
                                />
                            </ListItem>
                        ))}
                    </List>
                </div>
            </div>
        </div>
    );
}
