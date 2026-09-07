import 'package:flutter/material.dart';
import 'package:supabase_flutter/supabase_flutter.dart';

const supabaseUrl = 'https://bbicfqarichingoyvwkt.supabase.co';
const supabaseAnonKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJiaWNmcWFyaWNoaW5nb3l2d2t0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODg2OTIxNTIsImV4cCI6MjEwNDI2ODE1Mn0.Bpz779UnfrZJJfNFtLTATJPHJGrPe8jjjS4M1VzxFv4';

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();

  await Supabase.initialize(
    url: supabaseUrl,
    anonKey: supabaseAnonKey,
  );

  runApp(const IstqbTrainerApp());
}

final supabase = Supabase.instance.client;

class IstqbTrainerApp extends StatelessWidget {
  const IstqbTrainerApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'ISTQB Trainer',
      theme: ThemeData(
        primarySwatch: Colors.blueGrey,
        useMaterial3: true,
      ),
      home: const ConnectionTestScreen(),
    );
  }
}

class ConnectionTestScreen extends StatefulWidget {
  const ConnectionTestScreen({super.key});

  @override
  State<ConnectionTestScreen> createState() => _ConnectionTestScreenState();
}

class _ConnectionTestScreenState extends State<ConnectionTestScreen> {
  String _status = 'Teste Verbindung...';

  @override
  void initState() {
    super.initState();
    _testConnection();
  }

  Future<void> _testConnection() async {
    try {
      final response = await supabase
          .from('learning_objectives')
          .select()
          .limit(10);

      setState(() {
        _status = 'Verbindung erfolgreich! ${response.length} Learning Objectives gefunden.';
      });
    } catch (e) {
      setState(() {
        _status = 'Fehler: $e';
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('ISTQB Trainer')),
      body: Center(
        child: Padding(
          padding: const EdgeInsets.all(24.0),
          child: Text(
            _status,
            textAlign: TextAlign.center,
            style: const TextStyle(fontSize: 16),
          ),
        ),
      ),
    );
  }
}