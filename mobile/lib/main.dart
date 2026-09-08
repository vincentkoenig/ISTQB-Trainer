import 'package:flutter/material.dart';
import 'package:supabase_flutter/supabase_flutter.dart';
import 'practice_screen.dart';
import 'review_screen.dart';
import 'mock_exam_screen.dart';
import 'mock_exam_history_screen.dart';
import 'package:google_fonts/google_fonts.dart';

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
    // Modernere Palette: Indigo als Hauptfarbe, warmes Grün als Akzent
    const primaryColor = Color(0xFF4F46E5); // Indigo 600
    const primaryDark = Color(0xFF3730A3);
    const accentColor = Color(0xFF10B981); // Emerald 500
    const backgroundColor = Color(0xFFFAFAFC);
    const surfaceColor = Colors.white;

    final baseTextTheme = GoogleFonts.plusJakartaSansTextTheme();

    return MaterialApp(
      title: 'ISTQB Trainer',
      theme: ThemeData(
        useMaterial3: true,
        scaffoldBackgroundColor: backgroundColor,
        colorScheme: ColorScheme.fromSeed(
          seedColor: primaryColor,
          primary: primaryColor,
          secondary: accentColor,
          surface: surfaceColor,
        ),
        textTheme: baseTextTheme.copyWith(
          headlineSmall: GoogleFonts.plusJakartaSans(
            fontWeight: FontWeight.w700,
            fontSize: 22,
            letterSpacing: -0.5,
          ),
          titleMedium: GoogleFonts.plusJakartaSans(
            fontWeight: FontWeight.w700,
            fontSize: 16,
          ),
          bodyMedium: GoogleFonts.plusJakartaSans(
            fontSize: 14.5,
            height: 1.4,
          ),
          bodySmall: GoogleFonts.plusJakartaSans(
            fontSize: 12.5,
            color: Colors.grey.shade600,
          ),
        ),

        appBarTheme: AppBarTheme(
          backgroundColor: backgroundColor,
          foregroundColor: const Color(0xFF1F2937),
          elevation: 0,
          scrolledUnderElevation: 0,
          centerTitle: false,
          titleTextStyle: GoogleFonts.plusJakartaSans(
            fontSize: 20,
            fontWeight: FontWeight.w800,
            color: const Color(0xFF1F2937),
          ),
          iconTheme: const IconThemeData(color: Color(0xFF4F46E5)),
        ),

        cardTheme: CardThemeData(
          elevation: 0,
          color: surfaceColor,
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(18),
            side: BorderSide(color: Colors.grey.shade200, width: 1),
          ),
          margin: EdgeInsets.zero,
        ),

        elevatedButtonTheme: ElevatedButtonThemeData(
          style: ElevatedButton.styleFrom(
            backgroundColor: primaryColor,
            foregroundColor: Colors.white,
            padding: const EdgeInsets.symmetric(vertical: 15),
            shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(14),
            ),
            textStyle: GoogleFonts.plusJakartaSans(fontSize: 15, fontWeight: FontWeight.w700),
            elevation: 0,
          ),
        ),

        outlinedButtonTheme: OutlinedButtonThemeData(
          style: OutlinedButton.styleFrom(
            foregroundColor: primaryDark,
            backgroundColor: primaryColor.withValues(alpha: 0.06),
            side: BorderSide.none,
            padding: const EdgeInsets.symmetric(vertical: 15),
            shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(14),
            ),
            textStyle: GoogleFonts.plusJakartaSans(fontSize: 15, fontWeight: FontWeight.w700),
          ),
        ),

        inputDecorationTheme: InputDecorationTheme(
          border: OutlineInputBorder(
            borderRadius: BorderRadius.circular(14),
            borderSide: BorderSide.none,
          ),
          focusedBorder: OutlineInputBorder(
            borderRadius: BorderRadius.circular(14),
            borderSide: const BorderSide(color: primaryColor, width: 2),
          ),
          filled: true,
          fillColor: Colors.grey.shade100,
          contentPadding: const EdgeInsets.symmetric(horizontal: 16, vertical: 16),
        ),

        progressIndicatorTheme: const ProgressIndicatorThemeData(
          color: accentColor,
        ),

        chipTheme: ChipThemeData(
          selectedColor: primaryColor,
          backgroundColor: Colors.grey.shade100,
          labelStyle: GoogleFonts.plusJakartaSans(fontSize: 13, fontWeight: FontWeight.w600),
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(20),
          ),
          side: BorderSide.none,
        ),

        dividerTheme: DividerThemeData(color: Colors.grey.shade200, thickness: 1),
      ),
      home: const AuthGate(),
    );
  }
}

class AuthGate extends StatefulWidget {
  const AuthGate({super.key});

  @override
  State<AuthGate> createState() => _AuthGateState();
}

class _AuthGateState extends State<AuthGate> {
  @override
  Widget build(BuildContext context) {
    return StreamBuilder<AuthState>(
      stream: supabase.auth.onAuthStateChange,
      builder: (context, snapshot) {
        final session = supabase.auth.currentSession;
        if (session != null) {
          return const DashboardScreen();
        }
        return const LoginScreen();
      },
    );
  }
}

class LoginScreen extends StatefulWidget {
  const LoginScreen({super.key});

  @override
  State<LoginScreen> createState() => _LoginScreenState();
}

class _LoginScreenState extends State<LoginScreen> {
  final _emailController = TextEditingController();
  final _passwordController = TextEditingController();
  bool _isLoading = false;
  String? _errorMessage;

  Future<void> _login() async {
    setState(() {
      _isLoading = true;
      _errorMessage = null;
    });

    try {
      await supabase.auth.signInWithPassword(
        email: _emailController.text.trim(),
        password: _passwordController.text,
      );
    } on AuthException catch (e) {
      setState(() {
        _errorMessage = e.message;
      });
    } catch (e) {
      setState(() {
        _errorMessage = 'Unerwarteter Fehler: $e';
      });
    } finally {
      setState(() {
        _isLoading = false;
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: SingleChildScrollView(
          padding: const EdgeInsets.all(24.0),
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              const Text(
                'ISTQB Trainer',
                style: TextStyle(fontSize: 28, fontWeight: FontWeight.bold),
              ),
              const SizedBox(height: 32),
              TextField(
                controller: _emailController,
                decoration: const InputDecoration(
                  labelText: 'E-Mail',
                  border: OutlineInputBorder(),
                ),
                keyboardType: TextInputType.emailAddress,
              ),
              const SizedBox(height: 16),
              TextField(
                controller: _passwordController,
                decoration: const InputDecoration(
                  labelText: 'Passwort',
                  border: OutlineInputBorder(),
                ),
                obscureText: true,
              ),
              const SizedBox(height: 24),
              if (_errorMessage != null)
                Padding(
                  padding: const EdgeInsets.only(bottom: 16),
                  child: Text(
                    _errorMessage!,
                    style: const TextStyle(color: Colors.red),
                  ),
                ),
              SizedBox(
                width: double.infinity,
                child: ElevatedButton(
                  onPressed: _isLoading ? null : _login,
                  child: _isLoading
                      ? const CircularProgressIndicator()
                      : const Text('Anmelden'),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}

class DashboardScreen extends StatefulWidget {
  const DashboardScreen({super.key});

  @override
  State<DashboardScreen> createState() => _DashboardScreenState();
}

class _DashboardScreenState extends State<DashboardScreen> {
  List<Map<String, dynamic>> _dashboardData = [];
  bool _isLoading = true;

  @override
  void initState() {
    super.initState();
    _loadData();
  }

  Future<void> _loadData() async {
    final los = await supabase
        .from('learning_objectives')
        .select()
        .order('code', ascending: true);

    final allQuestions = await supabase
        .from('questions')
        .select('id, box, times_seen, next_review, chapters!inner(lo_id)');

    final nowUtc = DateTime.now().toUtc();

    final data = <Map<String, dynamic>>[];
    for (final lo in List<Map<String, dynamic>>.from(los)) {
      final loId = lo['id'];
      final questionsForLo = List<Map<String, dynamic>>.from(allQuestions)
          .where((q) => q['chapters']['lo_id'] == loId)
          .toList();

      final total = questionsForLo.length;
      final mastered = questionsForLo.where((q) => (q['box'] as int) >= 3).length;
      final notStarted = questionsForLo.where((q) => (q['times_seen'] as int) == 0).length;
      final box1Seen = questionsForLo
          .where((q) => (q['box'] as int) == 1 && (q['times_seen'] as int) > 0)
          .length;
      final box2 = questionsForLo.where((q) => (q['box'] as int) == 2).length;
      final box3 = questionsForLo.where((q) => (q['box'] as int) == 3).length;
      final box4 = questionsForLo.where((q) => (q['box'] as int) == 4).length;
      final box5 = questionsForLo.where((q) => (q['box'] as int) == 5).length;

      final dueCount = questionsForLo.where((q) {
        final nextReview = DateTime.parse(q['next_review'] as String);
        return nextReview.isBefore(nowUtc) || nextReview.isAtSameMomentAs(nowUtc);
      }).length;

      final percent = total > 0 ? ((mastered / total) * 100).round() : 0;

      data.add({
        'id': loId,
        'code': lo['code'],
        'title': lo['title'],
        'total': total,
        'mastered': mastered,
        'due_count': dueCount,
        'percent': percent,
        'not_started': notStarted,
        'box1_seen': box1Seen,
        'box2': box2,
        'box3': box3,
        'box4': box4,
        'box5': box5,
      });
    }

    setState(() {
      _dashboardData = data;
      _isLoading = false;
    });
  }

  Future<void> _logout() async {
    await supabase.auth.signOut();
  }

  Widget _buildBoxRow(String label, int count, Color color) {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 2),
      child: Row(
        children: [
          Container(
            width: 10,
            height: 10,
            decoration: BoxDecoration(color: color, shape: BoxShape.circle),
          ),
          const SizedBox(width: 8),
          Expanded(child: Text(label, style: const TextStyle(fontSize: 13))),
          Text('$count', style: const TextStyle(fontSize: 13, fontWeight: FontWeight.bold)),
        ],
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('ISTQB Trainer'),
        actions: [
          IconButton(
            icon: const Icon(Icons.quiz),
            tooltip: 'Prüfungssimulation',
            onPressed: () async {
              await Navigator.of(context).push(
                MaterialPageRoute(builder: (_) => const MockExamScreen()),
              );
              _loadData();
            },
          ),
          IconButton(
            icon: const Icon(Icons.history),
            tooltip: 'Prüfungsverlauf',
            onPressed: () {
              Navigator.of(context).push(
                MaterialPageRoute(builder: (_) => const MockExamHistoryScreen()),
              );
            },
          ),
          IconButton(
            icon: const Icon(Icons.logout),
            onPressed: _logout,
            tooltip: 'Abmelden',
          ),
        ],
      ),
      body: _isLoading
          ? const Center(child: CircularProgressIndicator())
          : RefreshIndicator(
              onRefresh: _loadData,
              child: ListView.builder(
                padding: const EdgeInsets.all(16),
                itemCount: _dashboardData.length,
                itemBuilder: (context, index) {
                  final lo = _dashboardData[index];
                  return Card(
                    margin: const EdgeInsets.only(bottom: 12),
                    child: Padding(
                      padding: const EdgeInsets.all(16),
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Text(
                            '${lo['code']} – ${lo['title']}',
                            style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 16),
                          ),
                          const SizedBox(height: 8),
                          ClipRRect(
                            borderRadius: BorderRadius.circular(4),
                            child: LinearProgressIndicator(
                              value: (lo['percent'] as int) / 100,
                              minHeight: 10,
                              backgroundColor: Colors.grey.shade200,
                            ),
                          ),
                          const SizedBox(height: 6),
                          Text('${lo['mastered']} von ${lo['total']} Fragen gemeistert (${lo['percent']}%)'),
                          const SizedBox(height: 10),
                          Container(
                            padding: const EdgeInsets.all(10),
                            decoration: BoxDecoration(
                              color: Colors.grey.shade100,
                              borderRadius: BorderRadius.circular(6),
                            ),
                            child: Column(
                              crossAxisAlignment: CrossAxisAlignment.start,
                              children: [
                                _buildBoxRow('Noch nie beantwortet', lo['not_started'], Colors.grey),
                                _buildBoxRow('Zuletzt falsch (Box 1)', lo['box1_seen'], Colors.red),
                                _buildBoxRow('Box 2', lo['box2'], Colors.orange),
                                _buildBoxRow('Box 3', lo['box3'], Colors.amber),
                                _buildBoxRow('Box 4', lo['box4'], Colors.lightGreen),
                                _buildBoxRow('Box 5 (sicher)', lo['box5'], Colors.green),
                              ],
                            ),
                          ),
                          const SizedBox(height: 6),
                          Text('${lo['due_count']} Frage(n) heute fällig', style: const TextStyle(color: Colors.grey)),
                          const SizedBox(height: 12),
                          Row(
                            children: [
                              Expanded(
                                child: ElevatedButton(
                                  onPressed: () async {
                                    await Navigator.of(context).push(
                                      MaterialPageRoute(
                                        builder: (_) => PracticeScreen(
                                          loId: lo['id'],
                                          loTitle: lo['title'],
                                        ),
                                      ),
                                    );
                                    _loadData();
                                  },
                                  child: const Text('Üben'),
                                ),
                              ),
                              const SizedBox(width: 8),
                              Expanded(
                                child: OutlinedButton(
                                  onPressed: () async {
                                    await Navigator.of(context).push(
                                      MaterialPageRoute(
                                        builder: (_) => ReviewScreen(
                                          loId: lo['id'],
                                          loTitle: lo['title'],
                                        ),
                                      ),
                                    );
                                    _loadData();
                                  },
                                  child: const Text('Fragen ansehen'),
                                ),
                              ),
                            ],
                          ),
                        ],
                      ),
                    ),
                  );
                },
              ),
            ),
    );
  }
}