import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:perplexity_clone/theme/colors.dart';
import 'package:perplexity_clone/widgets/search_bar_button.dart';

class SearchSection extends StatelessWidget {
  const SearchSection({super.key});

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.all(16.0),
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Padding(
            padding: const EdgeInsets.symmetric(vertical: 16.0),
            child: Text(
              "Where Knowledge Begins",
              style: GoogleFonts.ibmPlexMono(
                fontSize: 40,
                fontWeight: FontWeight.w400,
                height: 1.2,
                letterSpacing: -0.5,
              ),
            ),
          ),
          const SizedBox(height: 32),
          Container(
            width: 700,
            decoration: BoxDecoration(
              color: AppColors.searchBar,
              borderRadius: BorderRadius.circular(8),
              border: Border.all(
                color: AppColors.searchBarBorder,
                width: 1,
              ),
            ),
            child: Padding(
              padding: const EdgeInsets.all(16.0),
              child: Column(
                children: [
                  TextField(
                    decoration: InputDecoration(
                      hintText: "Search for anything...",
                      hintStyle: GoogleFonts.ibmPlexMono(
                        fontSize: 20,
                      ),
                      border: InputBorder.none,
                      isDense: true,
                      contentPadding: const EdgeInsets.all(0),
                    ),
                  ),
                  const SizedBox(height: 16),
                  Row(
                    children: [
                      SearchBarButton(
                        icon: Icons.auto_awesome_outlined,
                        text: 'Focus',
                      ),
                      const SizedBox(width: 12),
                      SearchBarButton(
                        icon: Icons.add_circle_outlined,
                        text: 'Attached',
                      ),
                      const Spacer(),
                      Container(
                        padding: const EdgeInsets.all(9),
                        decoration: BoxDecoration(
                          color: AppColors.submitButton,
                          borderRadius: BorderRadius.circular(40),
                        ),
                        child: const Icon(Icons.arrow_forward,
                            color: AppColors.background, size: 16),
                      )
                    ],
                  )
                ],
              ),
            ),
          )
        ],
      ),
    );
  }
}
